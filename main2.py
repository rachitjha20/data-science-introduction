from matplotlib import pyplot
import pandas as pd
import streamlit as st
import numpy as np
import altair as alt


st.image('2_dna.jpg',use_column_width=True)

st.write("""
# DNA Nucleotide Count Web App

This app's main function is to count composit of necleotide composition of query DNA.
""")

st.header('Enter DNA sequence')
sequence_input = ">DNA Query\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"
sequence = st.text_area("Sequence Input",sequence_input,height=250)
sequence = sequence.splitlines()

sequence = sequence[1:]
sequence = ''.join(sequence)

st.write("""
***
""")

st.header('Input (DNA Query)')
sequence

st.header('Output (DNA Necleotide Count)')

st.subheader('1. Print Dictionary')
def dna_necleotide_count(seq):
    d = dict([
        ('A',seq.count('A')),
        ('T',seq.count('T')),
        ('G',seq.count('G')),
        ('C',seq.count('C'))
    ])
    return d

x = dna_necleotide_count(sequence)
x

st.subheader('2. Print Text')
st.write('There are '+str(x['A'])+'adenine(A)')
st.write('There are '+str(x['T'])+'thmine(T)')
st.write('There are '+str(x['G'])+'Guanine(G)')
st.write('There are '+str(x['C'])+'Cytosine(C)')

st.subheader('3.Display Dataframe')
df = pd.DataFrame.from_dict(x,orient='index')
df = df.rename({0:'count'},axis='columns')
df.reset_index(inplace= True)
df = df.rename(columns = {'index':'nucleotide'})
st.write(df)

st.subheader('4. Display Bar Chart')
p = alt.Chart(df).mark_bar().encode(
    x='nucleotide',
    y='count'
    )

p = p.properties(
    width = alt.Step(80)
)
st.write(p)