import streamlit as st
import torch
# from diffusers import AutoPipelineForText2Image, LCMScheduler
from diffusers import AudioLDMPipeline, LCMScheduler

if "pipeline" not in st.session_state:
    #model name here
    model = 'cvssp/audioldm-s-full-v2'
    pipe = AudioLDMPipeline.from_pretrained(model, torch_dtype=torch.float16)
    # pipe = AutoPipelineForText2Image.from_pretrained(model, torch_dtype=torch.float16)
    pipe.to("cuda")
    pipe.scheduler = LCMScheduler.from_config(pipe.scheduler.config)
    st.session_state["pipeline"] = pipe

if "audios" not in st.session_state:
    st.session_state["audios"] = []


if prompt := st.text_input("Prompt"):
    with st.spinner("Generating..."):
        audios = st.session_state["pipeline"](prompt, num_inference_steps=8, guidance_scale=2, num_audios_per_prompt=1).audios
        print(audios)
        for audio in audios:
            st.session_state["audios"].append(audio)

#TODO: if change line 16
for audio in st.session_state["audios"][::-1]:
    st.audio(audio)