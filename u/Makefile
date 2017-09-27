LANGUAGE       = chef
DESIGN_PATTERN = conf
YAML           = bind.yml
SHORTDOMAIN    = 42algoritmos
DOMAIN         = $(SHORTDOMAIN).local
REVERSE        = 192

model = ../m
view  = ../v
SRCS  = $(shell find $(model) -name \*.tmpl -printf '%f\n' )

templates = $(foreach s,$(SRCS), $(addprefix $(view)/$(LANGUAGE)/$(DESIGN_PATTERN)/,$(s:.tmpl=.py)))
TARGETS   = $(templates)

all: $(TARGETS) view

# tmpl -> py
$(view)/$(LANGUAGE)/$(DESIGN_PATTERN)/%.py:  $(model)/%.tmpl
	cheetah-compile --flat $^ --odir $(view)/$(LANGUAGE)/$(DESIGN_PATTERN)

view:
	python app.py $(YAML)

clean:
	find $(view) -name "*.pyc" -delete
	find $(view) -name "*.py.bak" -delete
	find $(model) -type l -a -name "*.tmpl" -delete
	rm -rf $(view)/$(LANGUAGE)/$(DESIGN_PATTERN)
	rm -rf $(view)/$(LANGUAGE)
	ls | grep -vE '(Makefile|app.py|bind.yml)' | xargs rm

install:
	cp ./hosts /etc/
	cp ./interface /etc/network/
	cp ./enp1s0 /etc/network/interfaces.d/
	cp ./named.conf.local /etc/bind
	cp ./named.conf.options /etc/bind
	mkdir -p /etc/bind/$(SHORTDOMAIN)/
	cp ./db.$(DOMAIN) /etc/bind/$(SHORTDOMAIN)/
	cp ./db.$(REVERSE) /etc/bind/$(SHORTDOMAIN)/

restart:
	systemctl restart networking.service
	systemctl restart bind9.service

test:
	named-checkzone  $(DOMAIN) /etc/bind/$(SHORTDOMAIN)/db.$(DOMAIN)
	named-checkzone  $(DOMAIN) /etc/bind/$(SHORTDOMAIN)/db.$(REVERSE)
	host -l $(DOMAIN)
# END OF FILE
