
function cnoio_amass() {
    docker run -v /shared:/shared -v /root/.aws:/root/.aws -v /root/.principalmap:/root/.principalmap cnoio/amass $@
}

function cnoio_gobuster() {
    docker run -v /shared:/shared -v /root/.aws:/root/.aws -v /root/.principalmap:/root/.principalmap cnoio/gobuster $@
}

function cnoio_nimbusland() {
    docker run -v /shared:/shared -v /root/.aws:/root/.aws -v /root/.principalmap:/root/.principalmap cnoio/nimbusland $@
}

function cnoio_subjack() {
    docker run -v /shared:/shared -v /root/.aws:/root/.aws -v /root/.principalmap:/root/.principalmap cnoio/subjack $@
}

function cnoio_pyinstaller() {
    docker run -v /shared:/shared -v /root/.aws:/root/.aws -v /root/.principalmap:/root/.principalmap cnoio/pyinstaller $@
}

function cnoio_azureclione() {
    docker run -v /shared:/shared -v /root/.aws:/root/.aws -v /root/.principalmap:/root/.principalmap cnoio/azureclione $@
}

function cnoio_weirdaal() {
    docker run -v /shared:/shared -v /root/.aws:/root/.aws -v /root/.principalmap:/root/.principalmap cnoio/weirdaal $@
}

function cnoio_mintyoffline() {
    docker run -v /shared:/shared -v /root/.aws:/root/.aws -v /root/.principalmap:/root/.principalmap cnoio/mintyoffline $@
}

function cnoio_pmapper() {
    docker run -v /shared:/shared -v /root/.aws:/root/.aws -v /root/.principalmap:/root/.principalmap cnoio/pmapper $@
}

function cnoio_cosmik() {
    docker run -v /shared:/shared -v /root/.aws:/root/.aws -v /root/.principalmap:/root/.principalmap cnoio/cosmik $@
}

function cnoio_lolurslove() {
    docker run -v /shared:/shared -v /root/.aws:/root/.aws -v /root/.principalmap:/root/.principalmap cnoio/lolurslove $@
}

function cnoio_aws_inventory() {
    docker run -v /shared:/shared -v /root/.aws:/root/.aws -v /root/.principalmap:/root/.principalmap cnoio/aws_inventory $@
}