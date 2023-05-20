cryptsetup open --allow-discards $1 beterraba
mkdir -p /mnt/beterraba
mount  -o compress=zstd:1,subvol=home /dev/mapper/beterraba /mnt/beterraba
mount --bind /mnt/beterraba/shpnft/ /home/shpnft
