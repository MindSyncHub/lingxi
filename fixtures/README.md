# Fixtures

这里放 `一镜一梳` 用于验证、测试和验收的固定样本。

默认要求：

- 这里放“需要被重复验证”的固定样本
- 不直接存放后端运行时生成的解读记录
- 不把浏览器临时上传文件放到这里

如果样本来自一次联调或人工验收，应先脱敏，再整理成可复用 fixture 再进入本目录。

当前已沉淀：

> 注意：`toc-mvp/` 样本（画作照片与 golden 报告）因含真实用户画作与知识库衍生内容，未包含在开源版本中。

- `projects/aimandala/fixtures/manifest.yaml`
- `projects/aimandala/fixtures/toc-mvp/README.md`
- `projects/aimandala/fixtures/toc-mvp/toc-mvp-fixture-001.yaml`
- `projects/aimandala/fixtures/toc-mvp/toc-mvp-fixture-002.yaml`
- `projects/aimandala/fixtures/toc-mvp/toc-mvp-fixture-003.yaml`
- `projects/aimandala/fixtures/toc-mvp/toc-mvp-fixture-004.yaml`

最小校验命令：

- `python3 $REPO_ROOT/projects/aimandala/scripts/validate_fixtures.py`
