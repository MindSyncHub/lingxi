"""Shared pytest guards.

Some tests exercise the full interpretation pipeline, which requires:

- "generated prompt packs" (deploy-time artifacts compiled from a proprietary
  healing knowledge base), and/or
- the knowledge base source documents themselves
  (``docs/疗愈体系知识库/``).

Neither is part of the open source release. Tests that need them are skipped
automatically when the assets are absent, so the remaining suite stays green.
"""

from __future__ import annotations

from pathlib import Path

import pytest

_BACKEND_ROOT = Path(__file__).resolve().parents[1]
_AGENT_ROOT = _BACKEND_ROOT / "app" / "core" / "mandala_interpretation_agent"
_GENERATED_PACKS_ROOT = _AGENT_ROOT / "generated_prompt_packs"
_KNOWLEDGE_BASE_ROOT = _BACKEND_ROOT.parents[2] / "docs" / "疗愈体系知识库"

KNOWLEDGE_ASSETS_AVAILABLE = (
    (_GENERATED_PACKS_ROOT / "wealth-reasoning-v1.0.0").exists()
    and _KNOWLEDGE_BASE_ROOT.exists()
)

# (test file name, test function name) pairs that require the proprietary
# knowledge assets documented above.
_KNOWLEDGE_ASSET_TESTS = {
    ("test_api_routes_e2e.py", "test_create_app_loads_redeem_codes_before_route_authorization"),
    ("test_api_routes_e2e.py", "test_create_wealth_report_allows_pro_with_payment_bypassed"),
    ("test_api_routes_e2e.py", "test_create_wealth_report_returns_new_contract"),
    ("test_api_routes_e2e.py", "test_create_wealth_report_writes_followup_context"),
    ("test_api_routes_e2e.py", "test_get_wealth_report_reads_stored_artifact"),
    ("test_case_foundation_image_reading_runner.py", "test_load_complete_cases_can_filter_one_case"),
    ("test_case_foundation_image_reading_runner.py", "test_load_complete_cases_finds_all_11_cases"),
    ("test_case_foundation_image_reading_runner.py", "test_refresh_existing_reviews_uses_existing_foundation_json_without_model"),
    ("test_case_foundation_image_reading_runner.py", "test_render_review_markdown_contains_foundation_review_tables"),
    ("test_complete_case_wealth_report_regression_runner.py", "test_load_complete_cases_excludes_case_006"),
    ("test_mandala_ab_experiment_runner.py", "test_load_cases_defaults_to_case_001"),
    ("test_mandala_e2e_agent.py", "test_agent_selects_topic_prompt_pack_from_user_theme"),
    ("test_mandala_e2e_agent.py", "test_end_to_end_agent_returns_new_contract"),
    ("test_mandala_e2e_agent.py", "test_two_pass_rewrites_structured_visual_draft_to_markdown"),
    ("test_mandala_e2e_agent.py", "test_two_pass_visual_draft_does_not_leak_cross_circle_five_elements"),
    ("test_mandala_e2e_agent.py", "test_single_pass_agent_variant_generates_report_with_one_vision_text_call"),
    ("test_mandala_e2e_agent.py", "test_pro_report_mode_remains_internal_prelaunch"),
    ("test_mandala_e2e_agent.py", "test_foundation_prompt_pack_builder_uses_mandala_foundation_documents"),
    ("test_mandala_e2e_agent.py", "test_intimate_relationship_prompt_pack_builder_uses_topic_and_report_documents"),
    ("test_mandala_e2e_agent.py", "test_topic_prompt_pack_registry_covers_all_report_topics"),
    ("test_mandala_e2e_agent.py", "test_wealth_prompt_pack_builder_uses_topic_and_report_documents"),
    ("test_wealth_report.py", "test_native_wealth_runtime_routes_normalized_vision_model_language"),
    ("test_wealth_report.py", "test_native_wealth_runtime_routes_visual_observations"),
    ("test_wealth_report.py", "test_native_wealth_runtime_uses_yaml_match_keywords_for_expanded_routes"),
    ("test_wealth_report.py", "test_native_wealth_topic_context_uses_domain_name"),
    ("test_wealth_report_regression_runner.py", "test_build_agent_input_uses_wealth_theme"),
    ("test_wealth_report_regression_runner.py", "test_load_cases_from_wealth_regression_directory"),
}


def pytest_collection_modifyitems(items):
    if KNOWLEDGE_ASSETS_AVAILABLE:
        return
    for item in items:
        key = (Path(str(item.fspath)).name, item.name)
        if key in _KNOWLEDGE_ASSET_TESTS:
            item.add_marker(
                pytest.mark.skip(reason="requires proprietary knowledge assets (not included in the OSS release)")
            )
