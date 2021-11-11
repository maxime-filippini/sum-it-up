import hashlib

from notion.client import NotionClient
from notion.store import RecordStore


class ExtendedRecordStore(RecordStore):
    def call_load_page_chunk(self, page_id):

        if self._client.in_transaction():
            self._pages_to_refresh.append(page_id)
            return

        data = {
            "pageId": page_id,
            "limit": 100,
            "cursor": {"stack": []},
            "chunkNumber": 0,
            "verticalColumns": False,
        }

        recordmap = self._client.post("loadPageChunk", data).json()["recordMap"]

        self.store_recordmap(recordmap)


class ExtendedClient(NotionClient):
    def __init__(
        self,
        token_v2=None,
        monitor=False,
        start_monitoring=False,
        enable_caching=False,
        cache_key=None,
        email=None,
        password=None,
        client_specified_retry=None,
    ):
        super().__init__(
            token_v2=token_v2,
            monitor=monitor,
            start_monitoring=start_monitoring,
            enable_caching=enable_caching,
            cache_key=cache_key,
            email=email,
            password=password,
            client_specified_retry=client_specified_retry,
        )

        if enable_caching:
            cache_key = cache_key or hashlib.sha256(token_v2.encode()).hexdigest()
            self._store = ExtendedRecordStore(self, cache_key=cache_key)
        else:
            self._store = ExtendedRecordStore(self)

        self._update_user_info()
