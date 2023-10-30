echo GCLOUD_PROJECT="daniel-atwork-403505"
export GCLOUD_PROJECT="daniel-atwork-403505" 

echo REPO="website-docker-repo"
export REPO="website-docker-repo"

echo REGION="us-central1"
export REGION="us-central1"

echo IMAGE="website"
export IMAGE="website"

echo IMAGE_TAG=${REGION}-docker.pkg.dev/$GCLOUD_PROJECT/$REPO/$IMAGE
export IMAGE_TAG=${REGION}-docker.pkg.dev/$GCLOUD_PROJECT/$REPO/$IMAGE

# Build the image:
docker build -t $IMAGE_TAG -f Dockerfile --platform linux/x86_64 .
# Push it to Artifact Registry:
docker push $IMAGE_TAG

echo Pruning...
docker system prune -f
