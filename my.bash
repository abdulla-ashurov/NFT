# PUT NFT TO A BLOCKCHAIN
curl --request POST \
    --url 'https://api.nftport.xyz/v0/files' \
    --header 'Authorization: d580c132-0b1c-488d-8e25-ee5c49543315' \
    --header 'Content-Type: multipart/form-data' \
    --form 'file=@/Users/abdullaashurov/Desktop/NFT/NFT-image.webp;type=image/png'
