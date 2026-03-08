import json

from redteam.jailbreak_generator import generate_prompt


def test_generate_prompt_loads_from_prompt_file(monkeypatch, tmp_path):
    prompts = ["a", "b", "c"]
    prompts_dir = tmp_path / "prompts"
    prompts_dir.mkdir(parents=True)
    (prompts_dir / "jailbreak_prompts.json").write_text(json.dumps(prompts))

    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr("random.choice", lambda xs: xs[0])

    assert generate_prompt() == "a"
