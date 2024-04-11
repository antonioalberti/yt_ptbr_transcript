@echo off

REM Definir o nome do ambiente virtual
set VENV_NAME=myenv

REM Criar o ambiente virtual
python -m venv %VENV_NAME%

REM Ativar o ambiente virtual
call %VENV_NAME%\Scripts\activate.bat

REM Instalar os pacotes a partir do arquivo requirements.txt
pip install -r requirements.txt

REM Fazer o upgrade da biblioteca google-cloud-speech
pip install --upgrade google-cloud-speech

REM Mensagem de conclusão
echo Ambiente virtual criado e pacotes instalados com sucesso!
echo O ambiente virtual permanece ativado.

REM Manter o ambiente virtual ativado para uso posterior
