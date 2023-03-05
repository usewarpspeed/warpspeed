from marshmallow import fields, post_load
from galaxybrain.schemas import StepSchema, PolymorphicSchema


class PromptStepSchema(StepSchema):
    prompt_template = fields.Str(required=True)
    context = fields.Dict(keys=fields.Str(), values=fields.Raw())
    driver = fields.Nested(PolymorphicSchema(), allow_none=True)

    @post_load
    def make_step(self, data, **kwargs):
        from galaxybrain.steps import PromptStep

        return PromptStep(**data)
