@echo off
setLocal enabledelayedexpansion

echo   Gerador Executável Portátil (PyInstaller)
echo =============================================
echo.
echo Arquivos Python encontrados nessa pasta:
echo ---------------------------------------------

set count=0
for %%f in (*.py) do (
		set /a count+=1
		set "file!count!=%%f"
		echo !count! - %%f
)

if %count%==0 (
		echo [ERRO] Nenhum arquivo .py encontrado nessa pasta.
		pause
		exit
)

echo ---------------------------------------------
set /p choice="Digite o numero do arquivo que deseja converter: "

if not defined file%choice% (
		echo [ERRO] Opcao invalida.
		pause
		exit
)

set "target=!file%choice%!"

echo.
echo Convertendo "%target%" em executável...
echo Aguarde, pode levar um tempo...
echo.

python -m PyInstaller --onefile --noconsole "!target!"

echo.
echo ---------------------------------------------
echo  Processo concluido
echo  Seu .exe esta na pasta "dist"
echo ---------------------------------------------
pause
