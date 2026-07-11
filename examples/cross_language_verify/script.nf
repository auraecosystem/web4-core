#!/usr/bin/env nextflow

nextflow.enable.dsl = 2

params.vectors = "test_vectors"
params.outdir  = "results"

process VerifyRust {

    publishDir "${params.outdir}/rust", mode: 'copy'

    input:
    path vectors

    output:
    path "rust.json"

    script:
    """
    cargo run --release \
        --example verify \
        -- ${vectors} \
        > rust.json
    """
}

process VerifyPython {

    publishDir "${params.outdir}/python", mode: 'copy'

    input:
    path vectors

    output:
    path "python.json"

    script:
    """
    python verify.py ${vectors} > python.json
    """
}

process VerifyNode {

    publishDir "${params.outdir}/node", mode: 'copy'

    input:
    path vectors

    output:
    path "node.json"

    script:
    """
    node verify.js ${vectors} > node.json
    """
}

process VerifyGo {

    publishDir "${params.outdir}/go", mode: 'copy'

    input:
    path vectors

    output:
    path "go.json"

    script:
    """
    go run verify.go ${vectors} > go.json
    """
}

process VerifyJava {

    publishDir "${params.outdir}/java", mode: 'copy'

    input:
    path vectors

    output:
    path "java.json"

    script:
    """
    java -jar verifier.jar ${vectors} > java.json
    """
}

process VerifyDotNet {

    publishDir "${params.outdir}/dotnet", mode: 'copy'

    input:
    path vectors

    output:
    path "dotnet.json"

    script:
    """
    dotnet run --project verifier.csproj ${vectors} > dotnet.json
    """
}

process CompareResults {

    publishDir "${params.outdir}", mode: 'copy'

    input:
    path rust
    path python
    path node
    path go
    path java
    path dotnet

    output:
    path "verification_report.json"

    script:
    """
    python compare.py \
        $rust \
        $python \
        $node \
        $go \
        $java \
        $dotnet \
        > verification_report.json
    """
}

workflow {

    vectors = Channel.value(file(params.vectors))

    rust   = VerifyRust(vectors)
    python = VerifyPython(vectors)
    node   = VerifyNode(vectors)
    go     = VerifyGo(vectors)
    java   = VerifyJava(vectors)
    dotnet = VerifyDotNet(vectors)

    CompareResults(
        rust,
        python,
        node,
        go,
        java,
        dotnet
    )
}
