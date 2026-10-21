# Generated prompt packs (not included)

The packs in this directory are **deploy-time build artifacts** compiled from a
proprietary healing-knowledge base (translation tables, interpretation method
docs, exemplar case readings). They are intentionally **not part of the open
source release**.

- `topic_prompt_pack_registry.py` reads packs from here at runtime.
- Rebuild your own packs with `foundation_prompt_pack_builder.py` /
  `topic_prompt_pack_builder.py` / `wealth_prompt_pack_builder.py` against your
  own knowledge sources, or drop compiled packs into this directory.
- Unit tests that require real packs are skipped automatically when this
  directory is empty (see `tests/unit/test_mandala_e2e_agent.py`).
