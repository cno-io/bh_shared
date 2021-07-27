
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
    docker run -v /shared:/shared --entrypoint /bin/bash -ti cnoio/azureclione
}

function cnoio_weirdaal() {
    docker run -v /shared:/shared -v /root/.aws:/root/.aws -v /root/.principalmap:/root/.principalmap cnoio/weirdaal $@
}

function cnoio_mintyoffline() {
    docker run -v /shared:/shared -v /root/.aws:/root/.aws -v /root/.principalmap:/root/.principalmap cnoio/mintyoffline $@
}

function cnoio_pmapper() {
    docker run -v /shared:/shared -v /root/.aws:/root/.aws -v /root/.principalmap:/root/.principalmap --entrypoint /bin/bash -ti cnoio/pmapper
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

function cnoio_wfuzz() {
    docker run -v /shared:/shared -v /root/.aws:/root/.aws -v /root/.principalmap:/root/.principalmap cnoio/wfuzz $@
}

function cnoio_pacu() {
    docker run -v /shared:/shared -v /root/.aws:/root/.aws -v /root/.principalmap:/root/.principalmap -ti cnoio/pacu
}

function cnoio_gcpsagetatoken() {
    docker run -v /shared:/shared -ti cnoio/gcpsagetatoken $@
}

function cnoio_gcpbucketbrute() {
    docker run -it -v /root/.config/:/root/.config/ -v /shared/:/shared/ cnoio/gcpbucketbrute $@
}

function cnoio_scoutsuite() {
    docker run -it -v /root/.config/:/root/.config/ -v /root/.azure:/root/.azure -v /root/.aws:/root/.aws -v /shared/scoutsuite-report/:/root/scoutsuite-report/ -v /shared/:/shared/ cnoio/scoutsuite
}

function cnoio_evalshell() {
    docker run -v /shared:/shared -ti cnoio/evalshell $@
}

function cnoio_o365creeper() {
    docker run -v /shared:/shared -ti cnoio/o365creeper $@
}

function cnoio_voodooce() {
    docker run -ti -p 443:443 -p 995:995 -p 123:123/udp -v /shared:/shared -v /shared/voodoo_ce:/app/voodoo-ce cnoio/voodoo_ce
}

function cnoio_backup_voodooce() {
    docker run -ti -p 443:443 -p 995:995 -p 123:123/udp -v /shared:/shared cnoio/voodoo_ce
}

function cnoio_backup_voodooce2020() {
    docker run -ti -p 443:443 -p 995:995 -p 123:123/udp -v /shared:/shared cnoio/voodooce2020
}

function cnoio_sam() {
    docker run -v /shared:/shared -v /root/.aws:/root/.aws --entrypoint /bin/bash -ti cnoio/sam
}

function cnoio_impacket() {
    docker run -v /shared:/shared -v /root/.aws:/root/.aws -ti cnoio/impacket
}

function cnoio_mailsniper() {
    docker run -v /shared:/shared -v /root/.aws:/root/.aws -ti cnoio/mailsniper $@
}

function cnoio_roadrecon() {
    docker run -v /shared:/shared -p 5000:5000 -v /root/.aws:/root/.aws -ti cnoio/roadrecon $@
}

function cnoio_stormspotter-client() {
    docker run -v /shared:/shared -ti cnoio/stormspotter-client
}

function cnoio_stormspotter() {
    if [ -f /usr/local/bin/docker-compose ]
    then
        echo "Found docker-compose"
    else
        curl -L "https://github.com/docker/compose/releases/download/1.25.3/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
        chmod +x /usr/local/bin/docker-compose
        ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
    fi
    if [ -d "/shared/Stormspotter" ]
    then
        echo "Starting Stormspotter"
    else
        cd /shared
        git clone https://github.com/anthonyhendricksS2/Stormspotter.git
        cd /shared/Stormspotter
    fi

    cd /shared/Stormspotter &&	docker-compose up
}

alias docker-rm-all='docker rm $(docker ps -aq)'
alias docker-stop-all='docker stop $(docker ps -q)'
alias docker-force-rm-all='docker rm -f $(docker ps -aq)'
alias docker-volume-rm-all='docker volume rm $(docker volume ls -q)'
alias docker-rmi-all='docker rmi $(docker images -q)'
alias docker-force-rmi-all='docker rmi -f $(docker images -q)'
alias docker-force-container-prune='docker container prune -f'
alias docker-force-image-prune-all='docker image prune -f --all'
alias docker-shark-attack='docker-stop-all; docker-rm-all; docker-volume-rm-all; docker-rmi-all; docker-force-container-prune; docker-force-image-prune-all'
