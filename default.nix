with import <nixpkgs> {}; {
  legacyEnv = stdenv.mkDerivation {
    name = "legacy";
    buildInputs = [
      rPackages.devtools
    ];
    R_LIBS = "${rPackages.devtools}/library";
  };  
}
