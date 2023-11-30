POETRY ?= poetry
NPM ?= npm
NPX ?= npx

PYCACHE = $(shell find . -type d -name __pycache__)

.PHONY: install
install: _install_dev_packages _install_node_packages

.PHONY: install-ci
install-ci: _install_dev_packages _install_node_packages_ci

.PHONY: check
check:
	$(info [*] Running checks...)
	$(POETRY) run black --check .
	$(POETRY) run isort --check .
	$(NPX) prettier --check .

.PHONY: pretty
pretty:
	$(info [*] Prettying code...)
	$(POETRY) run black .
	$(POETRY) run isort .
	$(NPX) prettier --write .

.PHONY: check-update
check-update:
	$(POETRY) update --dry-run
	$(NPM) outdated -l || true

.PHONY: update
update:
	$(POETRY) update
	$(NPM) update

.PHONY: clean
clean: cdk.out $(wildcard *.egg-info) $(PYCACHE)
	$(RM) -r $^

.PHONY: _install_packages
_install_packages:
	$(info [*] Install required packages...)
	@$(POETRY) install --no-dev

.PHONY: _install_dev_packages
_install_dev_packages:
	$(info [*] Install required dev packages...)
	@$(POETRY) install

.PHONY: _install_node_packages
_install_node_packages:
	$(info [*] Install required node packages...)
	@$(NPM) install

.PHONY: _install_node_packages_ci
_install_node_packages_ci:
	$(info [*] Install required node packages...)
	@$(NPM) ci

print-%: ; @echo $*=$($*)
