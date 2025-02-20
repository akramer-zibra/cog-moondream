This is a simple prediction service for [moondream](https://github.com/vikhyat/moondream) which creates captions for given images either in short or long length.

## Prerequites
[cog](https://cog.run/getting-started/): which is a build tool to create docker images from `cog.yaml` definition
[moondream](https://moondream.ai/): which is the ai model for visual understanding download and gunzip into `./model` folder: https://github.com/vikhyat/moondream?tab=readme-ov-file#latest-model-checkpoints 

## Run
`cog predict -i image=http://...`  
or `cog predict -i image=@images.jpg`   

## Serve
### with cog
Start a prediction webservice: `cog serve` 

### with docker
Start temporary container from a prebuild image: `docker run --rm -d -p 5001:5000 cog-moondream:2B-int8-0.0.6`  
or `docker run --rm -d -p 5001:5000 cog-moondream:0_5B-int8-0.0.6` for the smaller 0.5B model version

Example request with an image URL:
```bash
curl --request POST \
  --url http://***.***.***.***:5001/predictions \
  --header 'content-type: application/json' \
  --data '{
    "input": {
      "image": "https://heise.cloudimg.io/v7/_www-heise-de_/imgs/18/4/8/0/4/8/4/7/hp-5512eb5e5134afa0.jpeg?org_if_sml=1&q=50&width=1600"
    }
}'
```

Example request with base64 encoded image data:
```bash
curl --request POST \
  --url http://***.***.***.***:5001/predictions \
  --header 'content-type: application/json' \
  --data '{
    "input": {
      "image": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAS0AAABqCAYAAADpyQeOAAAABHNCSVQICAgIfAhkiAAAABl0RVh0U29mdHdhcmUAZ25vbWUtc2NyZWVuc2hvdO8Dvz4AAAApdEVYdENyZWF0aW9uIF..."
    }
}'
```

## Build
Build a docker image: `cog build`
