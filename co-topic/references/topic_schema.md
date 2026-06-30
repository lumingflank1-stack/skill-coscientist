# Topic Generation Schema

## Topic Card

```markdown
### T1. Short Topic Name

- Distilled routine used:
- New biological context:
- Core mechanism:
- Why this is not just copying the source papers:
- Primary evidence:
- Evidence tier:
- Public datasets needed:
- Bioinformatics tests:
- Expected figure plan:
- Decisive experiment:
- Falsification criteria:
- Alternative explanation:
- Reviewer concern:
- Translational angle:
- Current status: candidate / prioritized / backup / rejected
```

## Topic Prioritization Columns

`rank,topic_id,topic_name,novelty,evidence,public_data_feasibility,analysis_feasibility,experiment_feasibility,causal_testability,manuscript_potential,total,decision,main_risk`

Score each numeric criterion from 1 to 5.

## Dataset Needs Columns

`topic_id,dataset_type,preferred_database,accession_if_known,species,tissue_or_cell_type,comparison,required_metadata,why_needed,minimum_success_condition`

## Experiment Needs

For each topic:

- Model.
- Perturbation.
- Rescue, if causal claim is intended.
- Controls.
- Readouts.
- Expected support result.
- Falsification result.
- Backup plan.

## Selection Brief

End with:

- Recommended main topic.
- Backup topic.
- Why the main topic is the best first test.
- What the user must choose next.
