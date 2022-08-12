
function cnoio_amass() {
    docker run --hostname cnoio_amass -v /shared:/shared -v /root/.aws:/root/.aws -v /root/.principalmap:/root/.principalmap cnoio/amass $@
}

function cnoio_gobuster() {
    docker run --hostname cnoio_gobuster -v /shared:/shared -v /root/.aws:/root/.aws -v /root/.principalmap:/root/.principalmap cnoio/gobuster $@
}

function cnoio_nimbusland() {
    docker run --hostname cnoio_nimbusland -v /shared:/shared -v /root/.aws:/root/.aws -v /root/.principalmap:/root/.principalmap cnoio/nimbusland $@
}

function cnoio_subjack() {
    docker run --hostname cnoio_subjack -v /shared:/shared -v /root/.aws:/root/.aws -v /root/.principalmap:/root/.principalmap cnoio/subjack $@
}

function cnoio_pyinstaller() {
    docker run --hostname cnoio_pyinstaller -v /shared:/shared -v /root/.aws:/root/.aws -v /root/.principalmap:/root/.principalmap cnoio/pyinstaller $@
}

function cnoio_azureclione() {
    docker run --hostname cnoio_azureclione -v /shared:/shared --entrypoint /bin/bash -ti cnoio/azureclione
}

function cnoio_weirdaal() {
    docker run --hostname cnoio_weirdaal -v /shared:/shared -v /root/.aws:/root/.aws -v /root/.principalmap:/root/.principalmap cnoio/weirdaal $@
}

function cnoio_mintyoffline() {
    docker run --hostname cnoio_mintyoffline -v /shared:/shared -v /root/.aws:/root/.aws -v /root/.principalmap:/root/.principalmap cnoio/mintyoffline $@
}

function cnoio_pmapper() {
    docker run --hostname cnoio_pmapper -v /shared:/shared -v /root/.aws:/root/.aws -v /root/.principalmap:/root/.principalmap --entrypoint /bin/bash -ti cnoio/pmapper
}

function cnoio_cosmik() {
    docker run --hostname cnoio_cosmik -v /shared:/shared -v /root/.aws:/root/.aws -v /root/.principalmap:/root/.principalmap cnoio/cosmik $@
}

function cnoio_lolurslove() {
    docker run --hostname cnoio_lolurslove -v /shared:/shared -v /root/.aws:/root/.aws -v /root/.principalmap:/root/.principalmap cnoio/lolurslove $@
}

function cnoio_aws_inventory() {
    docker run --hostname cnoio_aws_inventory -v /shared:/shared -v /root/.aws:/root/.aws -v /root/.principalmap:/root/.principalmap cnoio/aws_inventory $@
}

function cnoio_wfuzz() {
    docker run --hostname cnoio_wfuzz -v /shared:/shared -v /root/.aws:/root/.aws -v /root/.principalmap:/root/.principalmap cnoio/wfuzz $@
}

function cnoio_pacu() {
    docker run --hostname cnoio_pacu -v /shared:/shared -v /root/.aws:/root/.aws -v /root/.principalmap:/root/.principalmap -ti cnoio/pacu
}

function cnoio_gcpsagetatoken() {
    docker run --hostname cnoio_gcpsagetatoken -v /shared:/shared -ti cnoio/gcpsagetatoken $@
}

function cnoio_cloudenum() {
    docker run -it --hostname cnoio_cloudenum -v /root/.config/:/root/.config/ -v /shared/:/shared/ cnoio/cloud_enum $@
}

function cnoio_gcpbucketbrute() {
    docker run -it --hostname cnoio_gcpbucketbrute -v /root/.config/:/root/.config/ -v /shared/:/shared/ cnoio/gcpbucketbrute $@
}

function cnoio_scoutsuite() {
    docker run -it --hostname cnoio_scoutsuite -v /root/.config/:/root/.config/ -v /root/.azure:/root/.azure -v /root/.aws:/root/.aws -v /shared/scoutsuite-report/:/root/scoutsuite-report/ -v /shared/:/shared/ cnoio/scoutsuite
}

function cnoio_evalshell() {
    docker run --hostname cnoio_evalshell -v /shared:/shared -ti cnoio/evalshell $@
}

function cnoio_o365creeper() {
    docker run --hostname cnoio_o365creeper -v /shared:/shared -ti cnoio/o365creeper $@
}

function cnoio_voodooce() {
    docker run -ti --hostname cnoio_voodooce -p 443:443 -p 995:995 -p 123:123/udp -v /shared:/shared -v /shared/voodoo_ce:/app/voodoo-ce cnoio/voodoo_ce
}

function cnoio_backup_voodooce() {
    docker run -ti --hostname cnoio_backup_voodooce -p 443:443 -p 995:995 -p 123:123/udp -v /shared:/shared cnoio/voodoo_ce
}

function cnoio_backup_voodooce2020() {
    docker run -ti --hostname cnoio_voodooce2020 -p 443:443 -p 995:995 -p 123:123/udp -v /shared:/shared cnoio/voodooce2020
}

function cnoio_sam() {
    docker run --hostname cnoio_sam -v /shared:/shared -v /root/.aws:/root/.aws --entrypoint /bin/bash -ti cnoio/sam
}

function cnoio_impacket() {
    docker run --hostname cnoio_impacket -v /shared:/shared -v /root/.aws:/root/.aws -ti cnoio/impacket
}

function cnoio_mailsniper() {
    docker run --hostname cnoio_mailsniper -v /shared:/shared -v /root/.aws:/root/.aws -ti cnoio/mailsniper $@
}

function cnoio_roadrecon() {
    docker run --hostname cnoio_roadrecon -v /shared:/shared -p 5000:5000 -v /root/.aws:/root/.aws -ti cnoio/roadrecon $@
}

function cnoio_stormspotter-client() {
    docker run --hostname cnoio_stormspotter-client -v /shared:/shared -ti cnoio/stormspotter-client
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
