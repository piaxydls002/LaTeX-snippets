User Guide(Windows)
===================

Install Ubuntu on Windows
-------------------------
관리자 권한으로 명령프롬프트/PowerShell 실행 후
```powershell
wsl--install
```
입력 후 재부팅

Ubuntu 터미널에서 username/password 설정 후
```sh
sudo apt-get update
sudo apt-get upgrade
```
해주기

<!--
https://docs.microsoft.com/ko-kr/windows/wsl/install

Error Messages
--------------
+ `WSL optional component is not enabled`
  - 제어판-프로그램-windows 기능 켜기/끄기-Linux용 Windows 하위 시스템 체크 후 확인 및 재부팅
+ `Error: 0x800701bc WSL 2?????????https://aka.ms/wsl2kernel??????`
  - https://docs.microsoft.com/ko-kr/windows/wsl/install-manual 의 4번 항목에 있는 Linux 커널 업데이트 패키지를 다운받아 설치
-->

Install neovim
--------------
https://github.com/neovim/neovim/releases/latest
에서 제일 아래로 내려가서 nvim-linux64.deb 우클릭 후 링크 주소 복사

(2022-04-18 기준 `https://github.com/neovim/neovim/releases/download/v0.7.0/nvim-linux64.deb`)

```
wget (방금 복사한 링크)
sudo apt install ./nvim-linux64.deb
```
입력 후 `nvim` 치면 실행됨

Install neovim plugins
----------------------
+ vim-plug
```sh
sh -c 'curl -fLo "${XDG_DATA_HOME:-$HOME/.local/share}"/nvim/site/autoload/plug.vim --create-dirs \
       https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'
```
  - https://github.com/junegunn/vim-plug


User Guide(Linux)
=================

Guide to using Linux
====================

Guide to using Vim
==================
