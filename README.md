# docker-build-symlink

The sample how to work Docker with symbolic link.

Description in Japanese: [Qiita](https://qiita.com/kakken1988/items/787d89b659a0b9be4555)

## Build Dockerfile with symbolic link

Build

```sh
cd hello-world
tar -ch . | docker build -t docker-build-symlink -
```

Run

```sh
docker run docker-build-symlink
```

Cleanup

```sh
docker rmi --force docker-build-symlink
```
