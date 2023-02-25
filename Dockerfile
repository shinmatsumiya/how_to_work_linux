FROM ubuntu:20.04
# パッケージ管理ソフトのアップデート
RUN apt update

RUN ln -sf /usr/share/zoneinfo/Asia/Tokyo /etc/localtime

RUN apt install -y binutils
RUN apt install -y build-essential
RUN apt install -y golang
RUN apt install -y sysstat
RUN apt install -y python3-matplotlib
RUN apt install -y python3-pil
RUN apt install -y fonts-takao
RUN apt install -y fio
RUN apt install -y qemu-kvm
RUN apt install -y virt-manager
RUN apt install -y libvirt-clients
RUN apt install -y virtinst
RUN apt install -y jq
RUN apt install -y docker.io
RUN apt install -y containerd
RUN apt install -y libvirt-daemon-system
RUN apt install -y vim
RUN apt install -y strace
# RUN apt install -y psmisc

# vimのutf-8設定
COPY .vimrc /root/