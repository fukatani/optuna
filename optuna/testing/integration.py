import optuna


class DeterministicPruner(optuna.pruners.BasePruner):
    def __init__(self, is_pruning: bool) -> None:

        self.is_pruning = is_pruning

    def prune(self, study: "optuna.study.Study", trial: "optuna.trial.FrozenTrial") -> bool:

        return self.is_pruning


def create_running_trial(study: "optuna.study.Study", value: float) -> optuna.trial.Trial:

    trial_id = study._storage.create_new_trial(study._study_id)
    trial = study._storage.get_trial(trial_id)
    study._storage.set_trial_state_values(trial_id, state=trial.state, values=[value])
    return optuna.trial.Trial(study, trial_id)
