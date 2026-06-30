# Literature and Numbered Citation Rules

## Citation Ledger Columns

`citation_number,title,authors,year,journal,doi,pmid,url,claim_supported,evidence_type,notes`

## Numbered References

Create `references_numbered.md`:

```markdown
1. Authors. Title. Journal Year;volume:pages. DOI or PMID.
2. Authors. Title. Journal Year;volume:pages. DOI or PMID.
```

If bibliographic details are incomplete, include only verified fields and mark missing fields in `citation_ledger.csv`.

## In-Text Citations

Use citations in order of first appearance:

- Single citation: `[1]`
- Multiple citations: `[2,3]`
- Range only when the references are consecutive and truly support the same clause: `[4-6]`

## Search Targets

Search literature for:

- Broad disease or biological context.
- The specific cell type, pathway, molecule, metabolite, or public-data strategy.
- Conflicting evidence.
- Validation methods and prior perturbation studies.
- Clinical or translational relevance when claimed.

## Guardrails

- Do not invent references.
- Do not cite papers that were not read or at least metadata-verified.
- Do not use citations only for decoration.
- Prefer recent reviews for broad context and primary papers for specific mechanistic claims.
- Keep citation claims narrow: one citation should support the specific sentence where it appears.
