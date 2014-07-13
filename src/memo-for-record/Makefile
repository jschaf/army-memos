all:
	pandoc					\
	  --latex-engine=lualatex		\
	  --template=template.tex		\
          --variable fontsize=12pt		\
          --variable mainfont="TeX Gyre Termes"   \
          --variable sansfont="Helvetica Neue"	\
          --variable linestretch=1              \
          --variable graphics                   \
	  --no-tex-ligatures			\
	  --smart				\
	  -o mfr.tex				\
          mfr.md

	lualatex mfr.tex
