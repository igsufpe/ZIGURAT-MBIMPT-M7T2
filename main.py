"""
DataViz.MBIMPT-M7T2 — Painel de dados de modelos IFC com assistente de IA
ZIGURAT Institute of Technology · Professor: Ítalo Guedes

Arquivo ÚNICO e autocontido (logo e modelo de exemplo embutidos).

Executar localmente:
    pip install streamlit ifcopenshell pandas numpy plotly matplotlib reportlab pypdf requests
    streamlit run app.py

Streamlit Community Cloud: envie este arquivo + requirements.txt para um repositório GitHub
e aponte o app para app.py. (Opcional) defina LLM_API_KEY em Settings > Secrets.
"""
from __future__ import annotations

import base64
import hashlib
import html
import io
import json
import os
import random
import re
import tempfile
from datetime import datetime

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import requests
import streamlit as st

import ifcopenshell