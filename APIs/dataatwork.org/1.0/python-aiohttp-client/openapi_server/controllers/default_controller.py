from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.job import Job
from openapi_server.models.job_related_jobs import JobRelatedJobs
from openapi_server.models.job_skills import JobSkills
from openapi_server.models.normalized_job import NormalizedJob
from openapi_server.models.normalized_skill import NormalizedSkill
from openapi_server.models.skill import Skill
from openapi_server.models.skill_jobs import SkillJobs
from openapi_server.models.skill_related_skills import SkillRelatedSkills
from openapi_server import util


async def jobs_autocomplete_get(request: web.Request, begins_with=None, contains=None, ends_with=None) -> web.Response:
    """Job Title Autocomplete

    Retrieves the names, descriptions, and UUIDs of all job titles matching a given search criteria.

    :param begins_with: Find job titles beginning with the given text fragment
    :type begins_with: str
    :param contains: Find job titles containing the given text fragment
    :type contains: str
    :param ends_with: Find job titles ending with the given text fragment
    :type ends_with: str

    """
    return web.Response(status=200)


async def jobs_get(request: web.Request, offset=None, limit=None) -> web.Response:
    """Job Titles and Descriptions

    Retrieves the names, descriptions, and UUIDs of all job titles.

    :param offset: Pagination offset. Default is 0.
    :type offset: int
    :param limit: Maximum number of items per page. Default is 20 and cannot exceed 500.
    :type limit: int

    """
    return web.Response(status=200)


async def jobs_id_get(request: web.Request, id, fips=None) -> web.Response:
    """Job Title and Description

    Retrieves the name, description, and UUID of a job by specifying its O*NET SOC Code or UUID.

    :param id: The O*NET SOC Code or UUID of the job title to retrieve
    :type id: str
    :param fips: The FIPS Code of a Core-Based Statistical Area. Only return the job if present in this area
    :type fips: str

    """
    return web.Response(status=200)


async def jobs_id_related_jobs_get(request: web.Request, id) -> web.Response:
    """Jobs Associated with a Job

    Retrieves a collection of jobs associated with a specified job.

    :param id: The UUID of the job to retrieve related jobs for
    :type id: str

    """
    return web.Response(status=200)


async def jobs_id_related_skills_get(request: web.Request, id) -> web.Response:
    """Skills Associated with a Job

    Retrieves a collection of skills associated with a specified job.

    :param id: The UUID of the job to retrieve skills for
    :type id: str

    """
    return web.Response(status=200)


async def jobs_normalize_get(request: web.Request, job_title, limit=None) -> web.Response:
    """Job Title Normalization

    Retrieves the canonical job title for a synonymous job title

    :param job_title: Find the canonical job title(s) for jobs matching the given text fragment
    :type job_title: str
    :param limit: Maximumn number of job title synonyms to return. Default is 1 and cannot exceed 10.
    :type limit: int

    """
    return web.Response(status=200)


async def jobs_unusual_titles_get(request: web.Request, ) -> web.Response:
    """Unusual Job Titles

    Retrieves a list of unusual job titles and the UUIDs of their canonical jobs.


    """
    return web.Response(status=200)


async def skills_autocomplete_get(request: web.Request, begins_with=None, contains=None, ends_with=None) -> web.Response:
    """Skill Name Autocomplete

    Retrieves the names, descriptions, and UUIDs of all skills matching a given search criteria.

    :param begins_with: Find skill names beginning with the given text fragment
    :type begins_with: str
    :param contains: Find skill names containing the given text fragment
    :type contains: str
    :param ends_with: Find skill names ending with the given text fragment
    :type ends_with: str

    """
    return web.Response(status=200)


async def skills_get(request: web.Request, offset=None, limit=None) -> web.Response:
    """Skill Names and Descriptions

    Retrieve the names, descriptions, and UUIDs of all skills.

    :param offset: Pagination offset. Default is 0.
    :type offset: int
    :param limit: Maximum number of items per page. Default is 20 and cannot exceed 500.
    :type limit: int

    """
    return web.Response(status=200)


async def skills_id_get(request: web.Request, id) -> web.Response:
    """Skill Name and Description

    Retrieves the name, description, and UUID of a job by specifying its UUID.

    :param id: The UUID of the skill name to retrieve
    :type id: str

    """
    return web.Response(status=200)


async def skills_id_related_jobs_get(request: web.Request, id) -> web.Response:
    """Jobs Associated with a Skill

    Retrieves a collection of jobs associated with a specified skill.

    :param id: The UUID of the skill to retrieve jobs for
    :type id: str

    """
    return web.Response(status=200)


async def skills_id_related_skills_get(request: web.Request, id) -> web.Response:
    """Skills Associated with a Skill

    Retrieves a collection of skills associated with a specified skill.

    :param id: The UUID of the skill to retrieve related skills for
    :type id: str

    """
    return web.Response(status=200)


async def skills_normalize_get(request: web.Request, skill_name) -> web.Response:
    """Skill Name Normalization

    Retrieves the canonical skill name for a synonymous skill name

    :param skill_name: Find the canonical skill name(s) for skills matching the given text fragment
    :type skill_name: str

    """
    return web.Response(status=200)
