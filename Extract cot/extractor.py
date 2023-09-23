import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Defina a lista de símbolos de ações brasileiras desejadas
acoes_brasileiras = ['PETR4.SA', 'MGLU3.SA', 'HAPV3.SA', 'CIEL3.SA', 'B3SA3.SA', 'VIIA3.SA', 'ITSA4.SA',
                     'CVCB3.SA', 'VALE3.SA', 'BBDC4.SA', 'ITUB4.SA', 'AMER3.SA', 'ASAI3.SA', 'TRAD3.SA',
                     'BBAS3.SA', 'OIBR3.SA', 'PETR3.SA', 'ABEV3.SA', 'LREN3.SA', 'CPLE6.SA', 'COGN3.SA',
                     'GOLL4.SA', 'RAIZ4.SA', 'RAIL3.SA', 'SUZB3.SA', 'INTB3.SA', 'CSAN3.SA', 'MRVE3.SA',
                     'BRFS3.SA', 'BRKM5.SA', 'AZUL4.SA', 'AMAR3.SA', 'VBBR3.SA', 'CMIN3.SA', 'CEAB3.SA',
                     'EQTL3.SA', 'JBSS3.SA', 'ELET3.SA', 'SEQL3.SA', 'POMO4.SA', 'USIM5.SA', 'YDUQ3.SA',
                     'LIGT3.SA', 'GGBR4.SA', 'CCRO3.SA', 'EMBR3.SA', 'NTCO3.SA', 'PETZ3.SA', 'IFCM3.SA',
                     'CMIG4.SA', 'RENT3.SA', 'MRFG3.SA', 'ANIM3.SA', 'CBAV3.SA', 'GFSA3.SA', 'CYRE3.SA',
                     'SOMA3.SA', 'CRFB3.SA', 'BBSE3.SA', 'RRRP3.SA', 'CSNA3.SA', 'PRIO3.SA', 'LWSA3.SA',
                     'BBDC3.SA', 'WEGE3.SA', 'NEOE3.SA', 'ALPA4.SA', 'TIMS3.SA', 'TOTS3.SA', 'GMAT3.SA',
                     'ENEV3.SA', 'GOAU4.SA', 'ECOR3.SA', 'UGPA3.SA', 'FLRY3.SA', 'VAMO3.SA', 'QUAL3.SA',
                     'RADL3.SA', 'MULT3.SA', 'RDOR3.SA', 'BEEF3.SA', 'POSI3.SA', 'ODPV3.SA', 'TEND3.SA',
                     'JHSF3.SA', 'MODL3.SA', 'AERI3.SA', 'LJQQ3.SA', 'HBSA3.SA', 'STBP3.SA', 'MLAS3.SA',
                     'ALSO3.SA', 'SBSP3.SA', 'BRSR6.SA', 'ABCB4.SA', 'BPAN4.SA', 'CPFE3.SA', 'SLCE3.SA',
                     'DXCO3.SA', 'GUAR3.SA', 'ENBR3.SA', 'BRAP4.SA', 'KLBN4.SA', 'HYPE3.SA', 'CASH3.SA',
                     'MOVI3.SA', 'RAPT4.SA', 'DIRR3.SA', 'PLPL3.SA', 'CXSE3.SA', 'SAPR4.SA', 'RECV3.SA',
                     'TRPL4.SA', 'SIMH3.SA', 'VIVT3.SA', 'GGPS3.SA', 'IRBR3.SA', 'RANI3.SA', 'EZTC3.SA',
                     'SBFG3.SA', 'PCAR3.SA', 'PSSA3.SA', 'KEPL3.SA', 'SGPS3.SA', 'RCSL3.SA', 'DASA3.SA',
                     'ELET6.SA', 'EVEN3.SA', 'ONCO3.SA', 'MBLY3.SA', 'GRND3.SA', 'SMTO3.SA', 'SMFT3.SA',
                     'CURY3.SA', 'ENAT3.SA', 'BRIT3.SA', 'CPLE3.SA', 'PTBL3.SA', 'PGMN3.SA', 'LUPA3.SA',
                     'KRSA3.SA', 'HBOR3.SA', 'ARZZ3.SA', 'VIVA3.SA', 'NGRD3.SA', 'ESPA3.SA', 'CSMG3.SA',
                     'AESB3.SA', 'EGIE3.SA', 'BOAS3.SA', 'CAML3.SA', 'MYPK3.SA', 'AMBP3.SA', 'ALPK3.SA',
                     'ITUB3.SA', 'ZAMP3.SA', 'LAVV3.SA', 'LOGG3.SA', 'MEAL3.SA', 'VIVR3.SA', 'CMIG3.SA',
                     'LEVE3.SA', 'SEER3.SA', 'HBRE3.SA', 'AGRO3.SA', 'JALL3.SA', 'TRIS3.SA', 'SQIA3.SA',
                     'VVEO3.SA', 'MATD3.SA', 'TTEN3.SA', 'BMGB4.SA', 'ENJU3.SA', 'MDIA3.SA', 'UNIP6.SA',
                     'WIZC3.SA', 'TUPY3.SA', 'TASA4.SA', 'TECN3.SA', 'ITSA3.SA', 'SOJA3.SA', 'MILS3.SA',
                     'AZEV4.SA', 'BMOB3.SA', 'VULC3.SA', 'KLBN3.SA', 'INEP3.SA', 'VLID3.SA', 'ARML3.SA',
                     'SANB3.SA', 'PDTC3.SA', 'PNVL3.SA', 'SAPR3.SA', 'SANB4.SA', 'SHUL4.SA', 'TPIS3.SA',
                     'MDNE3.SA', 'WEST3.SA', 'OPCT3.SA', 'ETER3.SA', 'PINE4.SA', 'MELK3.SA', 'PORT3.SA',
                     'SHOW3.SA', 'MTRE3.SA', 'ROMI3.SA', 'PRNR3.SA', 'ORVR3.SA', 'JSLG3.SA', 'INEP4.SA',
                     'CSED3.SA', 'AALR3.SA', 'VITT3.SA', 'BLAU3.SA', 'FIQE3.SA', 'CTSA4.SA', 'NINJ3.SA',
                     'CLSA3.SA', 'FESA4.SA', 'TAEE4.SA', 'TCSA3.SA', 'LVTC3.SA', 'FRAS3.SA', 'DOTZ3.SA',
                     'USIM3.SA', 'RPMG3.SA', 'LPSB3.SA', 'ELMD3.SA', 'CTNM4.SA', 'PFRM3.SA', 'ALLD3.SA',
                     'IGTI3.SA', 'IGTI3.SA', 'CAMB3.SA', 'RNEW3.SA', 'BOBR4.SA', 'PDGR3.SA', 'HAGA4.SA',
                     'LOGN3.SA', 'RCSL4.SA', 'HAGA3.SA', 'BRAP3.SA', 'BRKM3.SA', 'OIBR4.SA', 'RNEW4.SA',
                     'AGXY3.SA', 'TFCO4.SA', 'RSID3.SA', 'SYNE3.SA', 'TAEE3.SA', 'CTSA3.SA', 'HOOT4.SA',
                     'DESK3.SA', 'PMAM3.SA', 'EUCA4.SA', 'BAHI3.SA', 'BRPR3.SA', 'BMEB4.SA', 'DEXP3.SA',
                     'TGMA3.SA', 'VSTE3.SA', 'AZEV3.SA', 'CSUD3.SA', 'ATMP3.SA', 'POMO3.SA', 'GOAU3.SA',
                     'IGTI4.SA', 'IGTI4.SA', 'GGBR3.SA', 'NEXP3.SA', 'FHER3.SA', 'RAPT3.SA', 'BIOM3.SA',
                     'UCAS3.SA', 'BEES3.SA', 'LAND3.SA', 'ALUP4.SA', 'AVLL3.SA', 'BEES4.SA', 'ENGI4.SA',
                     'CLSC4.SA', 'SLED4.SA', 'REDE3.SA', 'CEDO4.SA', 'DMVF3.SA', 'OSXB3.SA', 'COCE5.SA',
                     'APER3.SA', 'BRSR3.SA', 'TASA3.SA', 'SNSY5.SA', 'UNIP3.SA', 'WHRL4.SA', 'JFEN3.SA',
                     'ALUP3.SA', 'ATOM3.SA', 'RSUL4.SA', 'ENGI3.SA', 'EALT4.SA', 'CEBR6.SA', 'CGRA3.SA',
                     'ALPA3.SA', 'OFSA3.SA', 'BPAC3.SA', 'BPAC5.SA', 'RDNI3.SA', 'PTNT4.SA', 'MWET4.SA',
                     'EUCA3.SA', 'CGRA4.SA', 'CTNM3.SA', 'LUXM4.SA', 'CEBR5.SA', 'DEXP4.SA', 'SNSY3.SA',
                     'EQPA3.SA', 'TELB4.SA', 'CEDO3.SA', 'MTSA4.SA', 'BMEB3.SA', 'EMAE4.SA', 'CRPG5.SA',
                     'WLMM4.SA', 'SCAR3.SA', 'GSHP3.SA', 'WHRL3.SA', 'BAZA3.SA', 'HETA4.SA', 'PTNT3.SA',
                     'ENMT4.SA', 'TEKA4.SA', 'JOPA3.SA', 'ENMT3.SA', 'MNPR3.SA', 'DOHL4.SA', 'MNDL3.SA',
                     'CEBR3.SA', 'AFLT3.SA', 'CGAS5.SA', 'CRPG6.SA', 'BMIN4.SA', 'EALT3.SA', 'GEPA4.SA',
                     'MGEL4.SA', 'BSLI3.SA', 'BSLI4.SA', 'CTKA4.SA', 'SLED3.SA', 'CRIV4.SA', 'PEAB3.SA',
                     'TRPL3.SA', 'EPAR3.SA', 'CPLE5.SA', 'TELB3.SA', 'BGIP4.SA', 'BDLL4.SA', 'ESTR4.SA',
                     'FRTA3.SA', 'CGAS3.SA', 'HBTS5.SA', 'EKTR4.SA', 'EQMA3B.SA', 'BRSR5.SA', 'CBEE3.SA',
                     'PLAS3.SA', 'CRIV3.SA', 'MOAR3.SA', 'CEEB3.SA', 'PATI3.SA', 'CEED3.SA', 'BGIP3.SA',
                     'AHEB3.SA', 'AHEB6.SA', 'BALM3.SA', 'RPAD5.SA', 'BMKS3.SA', 'LIPR3.SA', 'PEAB4.SA',
                     'CRDE3.SA', 'UNIP5.SA', 'CSRN3.SA', 'NORD3.SA', 'BDLL3.SA', 'RPAD6.SA', 'ESTR3.SA',
                     'BRIV4.SA', 'BRIV3.SA', 'GEPA3.SA', 'CLSC3.SA', 'BALM4.SA', 'BRKM6.SA', 'BNBR3.SA',
                     'BAUH4.SA', 'CSRN6.SA', 'FESA3.SA', 'CRPG3.SA', 'CSRN5.SA', 'BRGE3.SA', 'USIM6.SA',
                     'RPAD3.SA', 'BMIN3.SA', 'TKNO4.SA', 'MERC4.SA', 'PATI4.SA', 'ELET5.SA', 'COCE3.SA',
                     'BRGE11.SA', 'BRGE8.SA', 'BRGE6.SA', 'FRIO3.SA', 'CALI3.SA', 'DTCY3.SA', 'MSPA4.SA',
                     'SOND5.SA', 'CSAB4.SA', 'MRSA6B.SA', 'CSAB3.SA', 'BRGE7.SA', 'AHEB5.SA', 'DOHL3.SA',
                     'JOPA4.SA', 'MWET3.SA', 'EKTR3.SA', 'BRGE12.SA', 'ODER4.SA', 'CEEB5.SA', 'EQPA7.SA',
                     'CASN3.SA', 'WLMM3.SA', 'MAPT4.SA', 'CEED4.SA', 'GPAR3.SA', 'MTSA3.SA', 'MAPT3.SA',
                     'DMFN3.SA', 'SOND6.SA', 'MRSA5B.SA', 'MSPA3.SA', 'EQPA5.SA', 'CTKA3.SA', 'BRGE5.SA',
                     'MRSA3B.SA', 'MERC3.SA', 'TCNO4.SA', 'TCNO3.SA', 'SHUL3.SA', 'FIGE3.SA', 'TEKA3.SA',
                     'HETA3.SA', 'SOND3.SA', 'CEGR3.SA', 'ECPR4.SA', 'EQPA6.SA', 'ECPR3.SA', 'CORR4.SA',
                     'SNSY6.SA', 'CASN4.SA', 'EMAE3.SA', 'VSPT3.SA', 'FIGE4.SA', 'LUXM3.SA', 'TKNO3.SA',
                     'COCE6.SA', 'MGEL3.SA']


resultados = []

for symbol in acoes_brasileiras:
    try:
        dados = yf.download(symbol, period="3d")
        ultimo_valor = dados["Close"].iloc[-1]
        # Cria um grafico pandas
        resultados.append({'Ação': symbol, 'Último Valor': ultimo_valor})

    except Exception as e:
        print(f"Erro ao obter os dados da ação {symbol}: {str(e)}")

dados_acoes = pd.DataFrame(resultados)
print(dados_acoes)

