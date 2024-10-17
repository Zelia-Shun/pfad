import streamlit as st
import torch
# from diffusers import AutoPipelineForText2Image, LCMScheduler
from diffusers import AudioLDMPipeline, LCMScheduler

if "pipeline" not in st.session_state:
    # load model
    model = 'cvssp/audioldm-s-full-v2'
    pipe = AudioLDMPipeline.from_pretrained(model, torch_dtype=torch.float32)
    pipe.to("cuda")

# generate audio with interface
if prompt := st.text_input("Prompt"):
    with st.spinner("Generating..."):
        audio = pipe(prompt, num_inference_steps=10, audio_length_in_s=5.0).audios[0]
        st.audio(data=audio, sample_rate=16000, autoplay=True)
