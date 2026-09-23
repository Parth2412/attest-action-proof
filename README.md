# attest Action proof

This public repository retains the release-gated evidence required by `attest` F11. It proves
that the published Action runs from a full commit SHA with least privilege, enforces independent
human review as a required check, and fails safely for an untrusted fork pull request.

The three onboarding files are generated unchanged by `attest init` from `attest-cli==0.1.0`.
The bootstrap workflow creates their pull request with the first-party `github-actions[bot]`
identity; the repository owner supplies the independent review.
