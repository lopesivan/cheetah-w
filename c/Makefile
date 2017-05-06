LANGUAGE       = java
DESIGN_PATTERN = af
YAML           = 1.yaml

model = ../m
view  = ../v
SRCS  = $(shell find $(model) -name \*.tmpl -printf '%f\n' )

templates = $(foreach s,$(SRCS), $(addprefix $(view)/$(LANGUAGE)/$(DESIGN_PATTERN)/,$(s:.tmpl=.py)))
TARGETS   = $(templates)

all: $(TARGETS)

# tmpl -> py
$(view)/$(LANGUAGE)/$(DESIGN_PATTERN)/%.py:  $(model)/%.tmpl
	cheetah-compile --flat $^ --odir $(view)/$(LANGUAGE)/$(DESIGN_PATTERN)

view:
	python parser.py $(view)/$(YAML)

clean:
	find $(view) -name "*.pyc" -delete
	find $(view) -name "*.py.bak" -delete
	find $(model) -type l -a -name "*.tmpl" -delete
	rm -rf $(view)/$(LANGUAGE)/$(DESIGN_PATTERN)
	rm -rf $(view)/$(LANGUAGE)

# END OF FILE

