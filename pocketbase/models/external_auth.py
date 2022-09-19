from typing import Any
from pocketbase.models.utils.base_model import BaseModel


class ExternalAuth(BaseModel):
    user_id: str
    provider: str
    provider_id: str

    def load(self, data: dict[str:Any]) -> None:
        super().load(data)
        self.user_id = data.get("userId", "")
        self.provider = data.get("provider", "")
        self.provider_id = data.get("providerId", "")
