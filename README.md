# :school: TCC PUC MG
## Pós Graduação em Ciência de Dados e Big Data :bar_chart: :books:
### PUC Minas - TCC Ciência de Dados e Big Data<br>

Tema: **PREVISÃO DE RISCO DE FRAUDES DE VALORAÇÃO EM IMPORTAÇÃO DE KITS DE TRANSMISSÃO DE MOTOCICLETAS**<br>
Leia o relatório completo do trabalho no arquivo _TCC Ciência de Dados - PUC MG - Carlos Eduardo Ribeiro Leite.pdf_

Vídeo de apresentação do trabalho: [YouTube](https://youtu.be/-BIbnZE2UVI)

## Estrutura do Projeto
```
Raiz
 ├── apresentação
 │    ├── Apresentação TCC Carlos Eduardo Ribeiro Leite.pdf
 │    └── Apresentação TCC Carlos Eduardo Ribeiro Leite HD.mp4
 ├── notebooks em html
 │    ├── 1a_trataCSVsSiscori.html
 │    ├── 1b_trataABIMOTO13.html
 │    ├── 2_geraWordclouds.html
 │    ├── 3_classificarAplicação.html
 │    ├── 4_classificarDESCRICAO.html
 │    ├── 5_NLP_modeloClassificador.html
 │    ├── 6_NLP_modeloClassificador_parteManual.html
 │    ├── 7_treinamentoClassificador.html
 │    └── 8_prediçãoRisco.html
 ├── notebooks em pdf
 │    ├── 1a_trataCSVsSiscori.pdf
 │    ├── 1b_trataABIMOTO13.pdf
 │    ├── 2_geraWordclouds.pdf
 │    ├── 3_classificarAplicação.pdf
 │    ├── 4_classificarDESCRICAO.pdf
 │    ├── 5_NLP_modeloClassificador.pdf
 │    ├── 6_NLP_modeloClassificador_parteManual.pdf
 │    ├── 7_treinamentoClassificador.pdf
 │    ├── 8_prediçãoRisco.pdf
 │    ├── funcoesTCC.pdf
 │    └── prettyPlotConfusionMatrix.pdf
 ├── notebooks
 │    ├── bases
 │    │    ├── siscori
 │    │    │    ├── siscori.zip.001
 │    │    │    ├── siscori.zip.002
 │    │    │    ├── siscori.zip.003
 │    │    │    ├── siscori.zip.004
 │    │    │    ├── siscori.zip.005
 │    │    │    ├── siscori.zip.006
 │    │    │    ├── siscori.zip.007
 │    │    │    ├── siscori.zip.008
 │    │    │    ├── siscori.zip.009
 │    │    │    ├── siscori.zip.010
 │    │    │    ├── siscori.zip.011
 │    │    │    ├── siscori.zip.012
 │    │    │    ├── siscori.zip.013
 │    │    │    ├── siscori.zip.014
 │    │    │    ├── siscori.zip.015
 │    │    │    ├── siscori.zip.016
 │    │    │    ├── siscori.zip.017
 │    │    │    ├── siscori.zip.018
 │    │    │    ├── siscori.zip.019
 │    │    │    ├── siscori.zip.020
 │    │    │    ├── siscori.zip.021
 │    │    │    ├── siscori.zip.022
 │    │    │    ├── siscori.zip.023
 │    │    │    ├── siscori.zip.024
 │    │    │    ├── siscori.zip.025
 │    │    │    ├── siscori.zip.026
 │    │    │    ├── siscori.zip.027
 │    │    │    ├── siscori.zip.028
 │    │    │    ├── siscori.zip.029
 │    │    │    └── siscori.zip.030
 │    │    ├── ABIMOTO13.xlsx
 │    │    ├── Aplicacoes.csv
 │    │    ├── dataframe.csv
 │    │    ├── dataframe.xlsx
 │    │    ├── dataframe_modelos.xlsx
 │    │    ├── dataframe_modelos_class0.csv
 │    │    ├── dataframe_modelos_class0.xlsx
 │    │    ├── dataframe_modelos_classificado.csv
 │    │    ├── dataframe_modelos_classificado.xlsx
 │    │    ├── dataframe_modelos_classificado_manual.csv
 │    │    ├── dataframe_modelos_classificado_manual.xlsx
 │    │    ├── dataframe_modelos_classificado_manual-tf.csv
 │    │    ├── dataframe_modelos_classificado_manual-tf.xlsx
 │    │    ├── dfABIMOTOv13.csv
 │    │    ├── dfABIMOTOv13.xlsx
 │    │    ├── palavrasChave.csv
 │    │    ├── sem_modelo.xlsx
 │    │    ├── siscori
 │    │    └── stopwords.csv
 │    ├── imagens
 │    │    ├── RelatórioRisco.png
 │    │    ├── wordcloud_descricoes_antes.png
 │    │    ├── wordcloud_descricoes_depois.png
 │    │    └── wordcloud_descricoes_final.png
 │    ├── pickle
 │    │    ├── clfsvc.pkl
 │    │    └── cvt.pkl
 │    ├── 1a_trataCSVsSiscori.ipynb
 │    ├── 1b_trataABIMOTO13.ipynb
 │    ├── 2_geraWordclouds.ipynb
 │    ├── 3_classificarAplicação.ipynb
 │    ├── 4_classificarDESCRICAO.ipynb
 │    ├── 5_NLP_modeloClassificador.ipynb
 │    ├── 6_NLP_modeloClassificador_parteManual.ipynb
 │    ├── 7_treinamentoClassificador.ipynb
 │    ├── 8_prediçãoRisco.ipynb
 │    ├── funcoesTCC.py
 │    └── prettyPlotConfusionMatrix.py
 ├── README.md
 └── TCC Ciência de Dados – PUC MG – Carlos Eduardo Ribeiro Leite.pdf
```

## Requisitos
 * [Python](https://www.python.org/) e algumas bibliotecas, como pandas, numpy e outras;
 * [Jupyter](https://jupyter.org/) ou uma ferramenta equivalente para execução de arquivos _"ipynb"_;
 * Descompactador de arquivos zip, como o [7-zip](https://www.7-zip.org/);
 * Leitor PDF, como o [Foxit PDF Reader](https://www.foxit.com/pdf-reader/); e
 * Player de vídeo MP4, como o [VLC media player](https://www.videolan.org/).

## Iniciando
 * Baixar ou clonar (via git) a pasta do projeto deste link [TCC PUC](https://github.com/kaduleite/TCC_PUC_MG_2021).
 * Descompactar os arquivos da base de dados contido em _/notebooks/bases/siscori_

## Executando Projeto
 * Excutar em sequência os notebooks na pasta _/notebooks_



