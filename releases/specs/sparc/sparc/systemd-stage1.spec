subarch: sparc
target: stage1
version_stamp: systemd-@TIMESTAMP@
rel_type: default
profile: default/linux/sparc/17.0/systemd
snapshot: @TIMESTAMP@
source_subpath: default/stage3-sparc-systemd-latest
compression_mode: pixz
update_seed: yes
update_seed_command: --update --deep --newuse @world
portage_confdir: @REPO_DIR@/releases/portage/stages
portage_prefix: releng
