INPUT := mcgrath
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
	rubber --pdf $(INPUT).tex

docx:
	pandoc					\
	  --smart				\
	  -o $(INPUT).docx				\
          $(INPUT).md
