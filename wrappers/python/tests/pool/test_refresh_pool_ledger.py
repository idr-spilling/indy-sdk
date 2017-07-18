from tests.utils import pool, storage
from indy.pool import refresh_pool_ledger
import pytest
import logging

logging.basicConfig(level=logging.DEBUG)


@pytest.yield_fixture(autouse=True)
def before_after_each():
    storage.cleanup()
    yield
    storage.cleanup()


@pytest.mark.asyncio
async def test_refresh_pool_ledger_works():
    handle = await pool.create_and_open_pool_ledger("pool_name")
    await refresh_pool_ledger(handle)
