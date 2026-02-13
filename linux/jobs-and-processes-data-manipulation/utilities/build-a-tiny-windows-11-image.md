---
author: codex
type: normal
category: how-to
tags:
  - linux
  - windows
  - tiny11
  - iso
  - wimlib
  - virtualization
notes: intermediate
practiceQuestion:
  formats:
    - type-in-the-gap
  context: relative
revisionQuestion:
  formats:
    - fill-in-the-gap
  context: relative
---

# Build a Tiny Windows 11 image

---

## Content

If you want a lighter Windows 11 install for testing in a VM, you can strip optional components from an official ISO and rebuild it.

> Only do this with a legally obtained Windows image and for personal/lab use.

A practical Linux workflow uses `wimlib` and `genisoimage`:

```bash
sudo apt update
sudo apt install wimtools genisoimage p7zip-full
```

Extract the ISO and mount `install.wim`:

```bash
7z x Win11.iso -oWin11-src
wimlib-imagex info Win11-src/sources/install.wim
```

Export only the edition you need (example: index `6`) and use a higher compression level:

```bash
wimlib-imagex export \
  Win11-src/sources/install.wim 6 \
  Win11-src/sources/install-mini.wim \
  --compress=LZX:100
mv Win11-src/sources/install-mini.wim Win11-src/sources/install.wim
```

Rebuild a bootable ISO:

```bash
genisoimage -U -b boot/etfsboot.com -no-emul-boot -boot-load-size 8 \
  -hide boot.catalog -udf -iso-level 4 -D -N -joliet-long -relaxed-filenames \
  -V "WIN11_MINI" -o Win11-mini.iso Win11-src
```

Before writing to USB media, boot the ISO in a VM and verify it reaches Windows Setup.

Example test with `qemu`:

```bash
qemu-system-x86_64 \
  -m 4096 -smp 4 -cpu host \
  -enable-kvm \
  -cdrom Win11-mini.iso \
  -boot d
```

If you prefer a GUI flow, create a new VM in `virt-manager`, attach `Win11-mini.iso`, and check that setup starts normally.

---

## Practice

Complete the command used to list Windows editions inside `install.wim`:

```bash
wimlib-imagex ??? Win11-src/sources/install.wim
```

- info
- export
- capture
- mount

---

## Revision

To create a smaller image from one edition in `install.wim`, use `wimlib-imagex` ???.

- export
- append
- apply
- split
