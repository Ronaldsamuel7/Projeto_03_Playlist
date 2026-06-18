import streamlit as st 

generos = {
    'Funk' : {
        'Mc Ig' : 'https://www.youtube.com/watch?v=a8cK8LopBf4&list=RDa8cK8LopBf4&start_radio=1',
        'Mc Hariel' : 'https://www.youtube.com/watch?v=mW8o_WDL91o&list=RDmW8o_WDL91o&start_radio=1'
    },
    'Sertanejo' : {
        'Jorge & Matheus' : 'https://www.youtube.com/watch?v=VWRkQARH-9o&list=RDVWRkQARH-9o&start_radio=1',
        'Henrique & Juliano' : 'https://www.youtube.com/watch?v=09TSrr4nAmo&list=RD09TSrr4nAmo&start_radio=1'
    },
    'Pagode' : {
        'Zeca Pagodinho' : 'https://www.youtube.com/watch?v=oTREAvZbmME',
        'Tiaguinho' : 'https://www.youtube.com/watch?v=qUqc_cYejX0'
    },
    'Forró' : {
        'Tarcisio' : 'https://www.youtube.com/watch?v=6yXpnlZVvXk&list=RD6yXpnlZVvXk&start_radio=1',
    }
}

st.sidebar.title('AUDIOWAVE')
st.sidebar.image('logo.png')

genero = st.sidebar.selectbox('Selecione um genero musical', generos.keys())
artista = st.sidebar.selectbox('Selecione um artista', generos[genero].keys())

st.title(artista)
video, sobre = st.tabs(['Videos', 'Sobre o artista'])

with video:
    st.video(generos[genero][artista])

with sobre:
    if artista == 'Mc Ig':
        st.markdown('''
                    MC IG é um cantor e compositor de funk paulista que ganhou destaque com músicas sobre a realidade das periferias, ostentação e vida urbana.

Ele se tornou um dos nomes mais populares do funk brasileiro nos anos 2020, acumulando milhões de ouvintes e visualizações nas plataformas digitais.
''')
        
    elif artista == 'Mc Hariel':
        st.markdown('''
                    MC Hariel é um cantor e compositor de funk de São Paulo conhecido por letras que abordam superação, cotidiano da periferia e reflexões sobre a vida.

Ele se consolidou como um dos principais nomes do funk consciente no Brasil, com diversos sucessos e uma grande base de fãs.
''')
        
    elif artista == 'Jorge & Matheus':
        st.markdown('''
                    Jorge & Mateus é uma das duplas sertanejas mais influentes do Brasil, conhecida por sucessos românticos e por ajudar a popularizar o sertanejo universitário.

Com uma carreira consolidada desde os anos 2000, acumula inúmeros hits, recordes de público e milhões de ouvintes nas plataformas digitais.
''')
        
    elif artista == 'Henrique & Juliano':
        st.markdown('''
                    Henrique & Juliano é uma das duplas sertanejas de maior sucesso do país, conhecida por músicas românticas e grandes hits que dominam rádios e plataformas de streaming.

Os irmãos conquistaram enorme popularidade na última década, tornando-se referência no sertanejo contemporâneo e reunindo milhões de fãs em todo o Brasil.
''')
    elif artista == 'Zeca Pagodinho':
        st.markdown('''
                    Zeca Pagodinho é um cantor e compositor brasileiro consagrado no samba, conhecido pelo carisma, autenticidade e sucessos que marcaram gerações.

Com uma carreira de décadas, tornou-se um dos maiores nomes da música popular brasileira, sendo referência no samba e no pagode.
''')
    
    elif artista == 'Tiaguinho':
        st.markdown('''
                    Thiaguinho é um cantor, compositor e apresentador brasileiro que se destacou no pagode, primeiro com o grupo Exaltasamba e depois em carreira solo.

Com diversos sucessos e milhões de fãs, tornou-se um dos principais nomes do pagode contemporâneo no Brasil.
''')
        
    elif artista == 'Tarcisio':
        st.markdown('''Tarcísio do Acordeon é um cantor, compositor e instrumentista brasileiro que ganhou destaque no forró e piseiro com músicas românticas e dançantes.

Com diversos sucessos nacionais, tornou-se um dos principais nomes da nova geração do forró, acumulando milhões de ouvintes e apresentações por todo o Brasil.
''')