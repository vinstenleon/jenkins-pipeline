node {
    checkout scm

    docker.withRegistry('https://registry.hub.docker.com', 'dockerhub_id') {

        def customImage = docker.build("vinsten99/pipeline")

        /* Push the container to the custom Registry */
        customImage.push()
    }
}