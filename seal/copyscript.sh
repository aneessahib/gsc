id=$(docker create gsc-seal_base)
docker cp $id:/gramine/app_files/entrypoint.manifest.sgx $(pwd)/entrypoint.manifest.sgx
docker cp $id:/gramine/app_files/entrypoint.sig $(pwd)/entrypoint.sig
docker rm -v $id
