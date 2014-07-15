INPUT := senior-parachutist
all:
	pandoc					\
	  --latex-engine=lualatex		\
	  --template=template.tex		\
          --variable fontsize=12pt		\
          --variable linestretch=1              \
          --variable graphics                   \
	  --no-tex-ligatures			\
	  --smart				\
	  -o $(INPUT).tex				\
          $(INPUT).md

	# sed -i '' -e '/.def.labelenumi/d'  \
        #           -e '/itemsep1pt/d'       \
        #      $(INPUT).tex
	lualatex $(INPUT).tex
