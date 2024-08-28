from openai import OpenAI
from openai.types.chat.completion_create_params import ResponseFormat


client = OpenAI(
    base_url = 'http://localhost:11434/v1',
    api_key='ollama', # required, but unused
)


response = client.chat.completions.create(
  model="llama3",
  messages=[
    {"role": "user", "content": """Using this content, tell me is this stored in my .venv virtual environment, or locally on my computer system. If it is stored on my computer system, then how can I make it so all items are stored only in the .venv folder and not outside of it: "
     pip install resume-parser
Collecting resume-parser
  Using cached resume_parser-0.8.4-py3-none-any.whl.metadata (3.7 kB)
Collecting docx2txt>=0.8 (from resume-parser)
  Using cached docx2txt-0.8-py3-none-any.whl
Collecting nltk>=3.5 (from resume-parser)
  Using cached nltk-3.9.1-py3-none-any.whl.metadata (2.9 kB)
Collecting numpy>=1.19.1 (from resume-parser)
  Using cached numpy-2.1.0-cp312-cp312-macosx_14_0_arm64.whl.metadata (60 kB)
Collecting pandas>=1.1.0 (from resume-parser)
  Using cached pandas-2.2.2-cp312-cp312-macosx_11_0_arm64.whl.metadata (19 kB)
Collecting pdfminer.six>=20200517 (from resume-parser)
  Using cached pdfminer.six-20240706-py3-none-any.whl.metadata (4.1 kB)
Collecting pdfplumber>=0.5.23 (from resume-parser)
  Using cached pdfplumber-0.11.4-py3-none-any.whl.metadata (41 kB)
Collecting phonenumbers>=8.12.7 (from resume-parser)
  Using cached phonenumbers-8.13.44-py2.py3-none-any.whl.metadata (10 kB)
Collecting spacy>=2.3.2 (from resume-parser)
  Using cached spacy-3.7.6.tar.gz (1.3 MB)
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Collecting stemming>=1.0.1 (from resume-parser)
  Using cached stemming-1.0.1.zip (13 kB)
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Collecting tika>=1.24 (from resume-parser)
  Using cached tika-2.6.0.tar.gz (27 kB)
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Requirement already satisfied: click in ./.venv/lib/python3.12/site-packages (from nltk>=3.5->resume-parser) (8.1.7)
Collecting joblib (from nltk>=3.5->resume-parser)
  Using cached joblib-1.4.2-py3-none-any.whl.metadata (5.4 kB)
Collecting regex>=2021.8.3 (from nltk>=3.5->resume-parser)
  Using cached regex-2024.7.24-cp312-cp312-macosx_11_0_arm64.whl.metadata (40 kB)
Requirement already satisfied: tqdm in ./.venv/lib/python3.12/site-packages (from nltk>=3.5->resume-parser) (4.66.5)
Collecting python-dateutil>=2.8.2 (from pandas>=1.1.0->resume-parser)
  Using cached python_dateutil-2.9.0.post0-py2.py3-none-any.whl.metadata (8.4 kB)
Collecting pytz>=2020.1 (from pandas>=1.1.0->resume-parser)
  Using cached pytz-2024.1-py2.py3-none-any.whl.metadata (22 kB)
Collecting tzdata>=2022.7 (from pandas>=1.1.0->resume-parser)
  Using cached tzdata-2024.1-py2.py3-none-any.whl.metadata (1.4 kB)
Collecting charset-normalizer>=2.0.0 (from pdfminer.six>=20200517->resume-parser)
  Using cached charset_normalizer-3.3.2-cp312-cp312-macosx_11_0_arm64.whl.metadata (33 kB)
Collecting cryptography>=36.0.0 (from pdfminer.six>=20200517->resume-parser)
  Using cached cryptography-43.0.0-cp39-abi3-macosx_10_9_universal2.whl.metadata (5.4 kB)
Collecting pdfminer.six>=20200517 (from resume-parser)
  Using cached pdfminer.six-20231228-py3-none-any.whl.metadata (4.2 kB)
Collecting Pillow>=9.1 (from pdfplumber>=0.5.23->resume-parser)
  Using cached pillow-10.4.0-cp312-cp312-macosx_11_0_arm64.whl.metadata (9.2 kB)
Collecting pypdfium2>=4.18.0 (from pdfplumber>=0.5.23->resume-parser)
  Using cached pypdfium2-4.30.0-py3-none-macosx_11_0_arm64.whl.metadata (48 kB)
Collecting spacy-legacy<3.1.0,>=3.0.11 (from spacy>=2.3.2->resume-parser)
  Using cached spacy_legacy-3.0.12-py2.py3-none-any.whl.metadata (2.8 kB)
Collecting spacy-loggers<2.0.0,>=1.0.0 (from spacy>=2.3.2->resume-parser)
  Using cached spacy_loggers-1.0.5-py3-none-any.whl.metadata (23 kB)
Collecting murmurhash<1.1.0,>=0.28.0 (from spacy>=2.3.2->resume-parser)
  Using cached murmurhash-1.0.10-cp312-cp312-macosx_11_0_arm64.whl.metadata (2.0 kB)
Collecting cymem<2.1.0,>=2.0.2 (from spacy>=2.3.2->resume-parser)
  Using cached cymem-2.0.8-cp312-cp312-macosx_11_0_arm64.whl.metadata (8.4 kB)
Collecting preshed<3.1.0,>=3.0.2 (from spacy>=2.3.2->resume-parser)
  Using cached preshed-3.0.9-cp312-cp312-macosx_11_0_arm64.whl.metadata (2.2 kB)
Collecting thinc<8.3.0,>=8.2.2 (from spacy>=2.3.2->resume-parser)
  Using cached thinc-8.2.5-cp312-cp312-macosx_11_0_arm64.whl.metadata (15 kB)
Collecting wasabi<1.2.0,>=0.9.1 (from spacy>=2.3.2->resume-parser)
  Using cached wasabi-1.1.3-py3-none-any.whl.metadata (28 kB)
Collecting srsly<3.0.0,>=2.4.3 (from spacy>=2.3.2->resume-parser)
  Using cached srsly-2.4.8-cp312-cp312-macosx_11_0_arm64.whl.metadata (20 kB)
Collecting catalogue<2.1.0,>=2.0.6 (from spacy>=2.3.2->resume-parser)
  Using cached catalogue-2.0.10-py3-none-any.whl.metadata (14 kB)
Collecting weasel<0.5.0,>=0.1.0 (from spacy>=2.3.2->resume-parser)
  Using cached weasel-0.4.1-py3-none-any.whl.metadata (4.6 kB)
Requirement already satisfied: typer<1.0.0,>=0.3.0 in ./.venv/lib/python3.12/site-packages (from spacy>=2.3.2->resume-parser) (0.12.5)
Collecting requests<3.0.0,>=2.13.0 (from spacy>=2.3.2->resume-parser)
  Using cached requests-2.32.3-py3-none-any.whl.metadata (4.6 kB)
Requirement already satisfied: pydantic!=1.8,!=1.8.1,<3.0.0,>=1.7.4 in ./.venv/lib/python3.12/site-packages (from spacy>=2.3.2->resume-parser) (2.8.2)
Collecting jinja2 (from spacy>=2.3.2->resume-parser)
  Using cached jinja2-3.1.4-py3-none-any.whl.metadata (2.6 kB)
Collecting setuptools (from spacy>=2.3.2->resume-parser)
  Using cached setuptools-74.0.0-py3-none-any.whl.metadata (6.7 kB)
Collecting packaging>=20.0 (from spacy>=2.3.2->resume-parser)
  Using cached packaging-24.1-py3-none-any.whl.metadata (3.2 kB)
Collecting langcodes<4.0.0,>=3.2.0 (from spacy>=2.3.2->resume-parser)
  Using cached langcodes-3.4.0-py3-none-any.whl.metadata (29 kB)
Collecting cffi>=1.12 (from cryptography>=36.0.0->pdfminer.six>=20200517->resume-parser)
  Using cached cffi-1.17.0-cp312-cp312-macosx_11_0_arm64.whl.metadata (1.5 kB)
Collecting language-data>=1.2 (from langcodes<4.0.0,>=3.2.0->spacy>=2.3.2->resume-parser)
  Using cached language_data-1.2.0-py3-none-any.whl.metadata (4.3 kB)
Requirement already satisfied: annotated-types>=0.4.0 in ./.venv/lib/python3.12/site-packages (from pydantic!=1.8,!=1.8.1,<3.0.0,>=1.7.4->spacy>=2.3.2->resume-parser) (0.7.0)
Requirement already satisfied: pydantic-core==2.20.1 in ./.venv/lib/python3.12/site-packages (from pydantic!=1.8,!=1.8.1,<3.0.0,>=1.7.4->spacy>=2.3.2->resume-parser) (2.20.1)
Requirement already satisfied: typing-extensions>=4.6.1 in ./.venv/lib/python3.12/site-packages (from pydantic!=1.8,!=1.8.1,<3.0.0,>=1.7.4->spacy>=2.3.2->resume-parser) (4.12.2)
Collecting six>=1.5 (from python-dateutil>=2.8.2->pandas>=1.1.0->resume-parser)
  Using cached six-1.16.0-py2.py3-none-any.whl.metadata (1.8 kB)
Requirement already satisfied: idna<4,>=2.5 in ./.venv/lib/python3.12/site-packages (from requests<3.0.0,>=2.13.0->spacy>=2.3.2->resume-parser) (3.8)
Collecting urllib3<3,>=1.21.1 (from requests<3.0.0,>=2.13.0->spacy>=2.3.2->resume-parser)
  Using cached urllib3-2.2.2-py3-none-any.whl.metadata (6.4 kB)
Requirement already satisfied: certifi>=2017.4.17 in ./.venv/lib/python3.12/site-packages (from requests<3.0.0,>=2.13.0->spacy>=2.3.2->resume-parser) (2024.7.4)
Collecting blis<0.8.0,>=0.7.8 (from thinc<8.3.0,>=8.2.2->spacy>=2.3.2->resume-parser)
  Using cached blis-0.7.11-cp312-cp312-macosx_11_0_arm64.whl.metadata (7.4 kB)
Collecting confection<1.0.0,>=0.0.1 (from thinc<8.3.0,>=8.2.2->spacy>=2.3.2->resume-parser)
  Using cached confection-0.1.5-py3-none-any.whl.metadata (19 kB)
Collecting numpy>=1.19.1 (from resume-parser)
  Using cached numpy-1.26.4-cp312-cp312-macosx_11_0_arm64.whl.metadata (61 kB)
Requirement already satisfied: shellingham>=1.3.0 in ./.venv/lib/python3.12/site-packages (from typer<1.0.0,>=0.3.0->spacy>=2.3.2->resume-parser) (1.5.4)
Requirement already satisfied: rich>=10.11.0 in ./.venv/lib/python3.12/site-packages (from typer<1.0.0,>=0.3.0->spacy>=2.3.2->resume-parser) (13.8.0)
Collecting cloudpathlib<1.0.0,>=0.7.0 (from weasel<0.5.0,>=0.1.0->spacy>=2.3.2->resume-parser)
  Using cached cloudpathlib-0.18.1-py3-none-any.whl.metadata (14 kB)
Collecting smart-open<8.0.0,>=5.2.1 (from weasel<0.5.0,>=0.1.0->spacy>=2.3.2->resume-parser)
  Using cached smart_open-7.0.4-py3-none-any.whl.metadata (23 kB)
Collecting MarkupSafe>=2.0 (from jinja2->spacy>=2.3.2->resume-parser)
  Using cached MarkupSafe-2.1.5-cp312-cp312-macosx_10_9_universal2.whl.metadata (3.0 kB)
Collecting pycparser (from cffi>=1.12->cryptography>=36.0.0->pdfminer.six>=20200517->resume-parser)
  Using cached pycparser-2.22-py3-none-any.whl.metadata (943 bytes)
Collecting marisa-trie>=0.7.7 (from language-data>=1.2->langcodes<4.0.0,>=3.2.0->spacy>=2.3.2->resume-parser)
  Using cached marisa_trie-1.2.0-cp312-cp312-macosx_11_0_arm64.whl.metadata (8.7 kB)
Requirement already satisfied: markdown-it-py>=2.2.0 in ./.venv/lib/python3.12/site-packages (from rich>=10.11.0->typer<1.0.0,>=0.3.0->spacy>=2.3.2->resume-parser) (3.0.0)
Requirement already satisfied: pygments<3.0.0,>=2.13.0 in ./.venv/lib/python3.12/site-packages (from rich>=10.11.0->typer<1.0.0,>=0.3.0->spacy>=2.3.2->resume-parser) (2.18.0)
Collecting wrapt (from smart-open<8.0.0,>=5.2.1->weasel<0.5.0,>=0.1.0->spacy>=2.3.2->resume-parser)
  Using cached wrapt-1.16.0-cp312-cp312-macosx_11_0_arm64.whl.metadata (6.6 kB)
Requirement already satisfied: mdurl~=0.1 in ./.venv/lib/python3.12/site-packages (from markdown-it-py>=2.2.0->rich>=10.11.0->typer<1.0.0,>=0.3.0->spacy>=2.3.2->resume-parser) (0.1.2)
Using cached resume_parser-0.8.4-py3-none-any.whl (9.2 MB)
Using cached nltk-3.9.1-py3-none-any.whl (1.5 MB)
Using cached pandas-2.2.2-cp312-cp312-macosx_11_0_arm64.whl (11.3 MB)
Using cached pdfplumber-0.11.4-py3-none-any.whl (59 kB)
Using cached pdfminer.six-20231228-py3-none-any.whl (5.6 MB)
Using cached phonenumbers-8.13.44-py2.py3-none-any.whl (2.6 MB)
Using cached catalogue-2.0.10-py3-none-any.whl (17 kB)
Using cached charset_normalizer-3.3.2-cp312-cp312-macosx_11_0_arm64.whl (119 kB)
Using cached cryptography-43.0.0-cp39-abi3-macosx_10_9_universal2.whl (6.2 MB)
Using cached cymem-2.0.8-cp312-cp312-macosx_11_0_arm64.whl (41 kB)
Using cached langcodes-3.4.0-py3-none-any.whl (182 kB)
Using cached murmurhash-1.0.10-cp312-cp312-macosx_11_0_arm64.whl (26 kB)
Using cached packaging-24.1-py3-none-any.whl (53 kB)
Using cached pillow-10.4.0-cp312-cp312-macosx_11_0_arm64.whl (3.4 MB)
Using cached preshed-3.0.9-cp312-cp312-macosx_11_0_arm64.whl (128 kB)
Using cached pypdfium2-4.30.0-py3-none-macosx_11_0_arm64.whl (2.7 MB)
Using cached python_dateutil-2.9.0.post0-py2.py3-none-any.whl (229 kB)
Using cached pytz-2024.1-py2.py3-none-any.whl (505 kB)
Using cached regex-2024.7.24-cp312-cp312-macosx_11_0_arm64.whl (279 kB)
Using cached requests-2.32.3-py3-none-any.whl (64 kB)
Using cached spacy_legacy-3.0.12-py2.py3-none-any.whl (29 kB)
Using cached spacy_loggers-1.0.5-py3-none-any.whl (22 kB)
Using cached srsly-2.4.8-cp312-cp312-macosx_11_0_arm64.whl (486 kB)
Using cached thinc-8.2.5-cp312-cp312-macosx_11_0_arm64.whl (760 kB)
Using cached numpy-1.26.4-cp312-cp312-macosx_11_0_arm64.whl (13.7 MB)
Using cached tzdata-2024.1-py2.py3-none-any.whl (345 kB)
Using cached wasabi-1.1.3-py3-none-any.whl (27 kB)
Using cached weasel-0.4.1-py3-none-any.whl (50 kB)
Using cached jinja2-3.1.4-py3-none-any.whl (133 kB)
Using cached joblib-1.4.2-py3-none-any.whl (301 kB)
Using cached setuptools-74.0.0-py3-none-any.whl (1.3 MB)
Using cached blis-0.7.11-cp312-cp312-macosx_11_0_arm64.whl (1.1 MB)
Using cached cffi-1.17.0-cp312-cp312-macosx_11_0_arm64.whl (178 kB)
Using cached cloudpathlib-0.18.1-py3-none-any.whl (47 kB)
Using cached confection-0.1.5-py3-none-any.whl (35 kB)
Using cached language_data-1.2.0-py3-none-any.whl (5.4 MB)
Using cached MarkupSafe-2.1.5-cp312-cp312-macosx_10_9_universal2.whl (18 kB)
Using cached six-1.16.0-py2.py3-none-any.whl (11 kB)
Using cached smart_open-7.0.4-py3-none-any.whl (61 kB)
Using cached urllib3-2.2.2-py3-none-any.whl (121 kB)
Using cached marisa_trie-1.2.0-cp312-cp312-macosx_11_0_arm64.whl (173 kB)
Using cached pycparser-2.22-py3-none-any.whl (117 kB)
Using cached wrapt-1.16.0-cp312-cp312-macosx_11_0_arm64.whl (38 kB)
Building wheels for collected packages: spacy, stemming, tika
  Building wheel for spacy (pyproject.toml) ... done
  Created wheel for spacy: filename=spacy-3.7.6-cp312-cp312-macosx_14_0_arm64.whl size=5924524 sha256=e1d50c56929d35415aab39b1670af5e39d63fdc6aeb972e22dc702d98ce14952
  Stored in directory: /Users/sulaiman/Library/Caches/pip/wheels/81/45/eb/88dd77a5cba760a99df76c0d330a990c15fff4e01f41d431fe
  Building wheel for stemming (pyproject.toml) ... done
  Created wheel for stemming: filename=stemming-1.0.1-py3-none-any.whl size=11123 sha256=0fb0d06bae2ab5efd284649853f363676fb43150fd599d1c5a572f4993ab816c
  Stored in directory: /Users/sulaiman/Library/Caches/pip/wheels/20/d4/73/028ca44cd75949ad81250dd3ecea7e4c61b97672587b65ef35
  Building wheel for tika (pyproject.toml) ... done
  Created wheel for tika: filename=tika-2.6.0-py3-none-any.whl size=32624 sha256=396fc562008bf99d0ff61539b94c021df6392829b2a46958be73b56e5dba9b91
  Stored in directory: /Users/sulaiman/Library/Caches/pip/wheels/ad/75/cc/cb91a96aab7a28cac9a04967c6034162d50dd441c1709aeea7
Successfully built spacy stemming tika
Installing collected packages: stemming, pytz, phonenumbers, docx2txt, cymem, wrapt, wasabi, urllib3, tzdata, spacy-loggers, spacy-legacy, six, setuptools, regex, pypdfium2, pycparser, Pillow, packaging, numpy, murmurhash, MarkupSafe, joblib, cloudpathlib, charset-normalizer, catalogue, srsly, smart-open, requests, python-dateutil, preshed, nltk, marisa-trie, jinja2, cffi, blis, tika, pandas, language-data, cryptography, confection, weasel, thinc, pdfminer.six, langcodes, spacy, pdfplumber, resume-parser
Successfully installed MarkupSafe-2.1.5 Pillow-10.4.0 blis-0.7.11 catalogue-2.0.10 cffi-1.17.0 charset-normalizer-3.3.2 cloudpathlib-0.18.1 confection-0.1.5 cryptography-43.0.0 cymem-2.0.8 docx2txt-0.8 jinja2-3.1.4 joblib-1.4.2 langcodes-3.4.0 language-data-1.2.0 marisa-trie-1.2.0 murmurhash-1.0.10 nltk-3.9.1 numpy-1.26.4 packaging-24.1 pandas-2.2.2 pdfminer.six-20231228 pdfplumber-0.11.4 phonenumbers-8.13.44 preshed-3.0.9 pycparser-2.22 pypdfium2-4.30.0 python-dateutil-2.9.0.post0 pytz-2024.1 regex-2024.7.24 requests-2.32.3 resume-parser-0.8.4 setuptools-74.0.0 six-1.16.0 smart-open-7.0.4 spacy-3.7.6 spacy-legacy-3.0.12 spacy-loggers-1.0.5 srsly-2.4.8 stemming-1.0.1 thinc-8.2.5 tika-2.6.0 tzdata-2024.1 urllib3-2.2.2 wasabi-1.1.3 weasel-0.4.1 wrapt-1.16.0"
  """}
  ]
)
print(response.choices[0].message.content)
# print(response)