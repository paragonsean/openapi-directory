# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_exception import ApiException
from openapi_server.models.default_response_dtoof_boolean import DefaultResponseDTOOfBoolean
from openapi_server.models.default_response_dtoof_list_of_package_search_dto import DefaultResponseDTOOfListOfPackageSearchDTO
from openapi_server.models.default_response_dtoof_package_dto import DefaultResponseDTOOfPackageDTO
from openapi_server.models.default_response_dtoof_package_search_dto import DefaultResponseDTOOfPackageSearchDTO
from openapi_server.models.default_response_dtoof_status_dto import DefaultResponseDTOOfStatusDTO
from openapi_server.models.default_response_dtoof_string import DefaultResponseDTOOfString
from openapi_server.models.package_dto import PackageDTO


pytestmark = pytest.mark.asyncio

async def test_package_delete(client):
    """Test case for package_delete

    Delete existing package             
    """
    params = [('PackageId', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/Package',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_package_get(client):
    """Test case for package_get

    Get package details by packageId             
    """
    params = [('packageId', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/Package',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_package_post(client):
    """Test case for package_post

    Insert new package into the system             
    """
    body = {"isShownInMobile":True,"modifiedUser":"modifiedUser","endDate":"2000-01-23T04:56:07.000+00:00","memberCanRemoveAddOns":True,"totalPrice":5.025004791520295,"description":"description","expireInMonths":3,"isActive":True,"packageType":"packageType","packageNumber":"packageNumber","isAutoRenew":True,"bindingPeriod":9,"features":"features","addonFee":7.061401241503109,"maximumGiveAwayRestAmount":4.145608029883936,"perVisitPrice":7.457744773683766,"packageName":"packageName","instructionsToGymUsers":"instructionsToGymUsers","availableGyms":[{"gymId":1,"gymName":"gymName","externalGymNumber":6,"location":"location"},{"gymId":1,"gymName":"gymName","externalGymNumber":6,"location":"location"}],"createdUser":"createdUser","monthlyFee":7.386281948385884,"nextPackageNumber":1,"isFirstMonthFree":True,"numberOfVisits":1,"serviceFee":4.965218492984954,"freeMonths":2,"registrationFee":1.1730742509559433,"addOns":[{"articleName":"articleName","endOrder":5,"isIncludeServiceInCharge":True,"articleNumber":6,"startOrder":2,"numberOfItems":5.637376656633329,"articleId":0,"articlePrice":1.4658129805029452,"measureUnit":"measureUnit"},{"articleName":"articleName","endOrder":5,"isIncludeServiceInCharge":True,"articleNumber":6,"startOrder":2,"numberOfItems":5.637376656633329,"articleId":0,"articlePrice":1.4658129805029452,"measureUnit":"measureUnit"}],"packageId":6,"isRegistrationFee":True,"isRestAmount":True,"isSponsorPackage":True,"tags":"tags","createdDate":"2000-01-23T04:56:07.000+00:00","instructionsToWebUsers":"instructionsToWebUsers","numberOfInstallments":1,"isAtg":True,"memberCanAddAddOns":True,"modifiedDate":"2000-01-23T04:56:07.000+00:00","memberCanLeaveWithinFreePeriod":True,"applyForAllGyms":True,"shownInWeb":True,"startDate":"2000-01-23T04:56:07.000+00:00"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/Package',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_package_put(client):
    """Test case for package_put

    Update existing package by its ID             
    """
    body = {"isShownInMobile":True,"modifiedUser":"modifiedUser","endDate":"2000-01-23T04:56:07.000+00:00","memberCanRemoveAddOns":True,"totalPrice":5.025004791520295,"description":"description","expireInMonths":3,"isActive":True,"packageType":"packageType","packageNumber":"packageNumber","isAutoRenew":True,"bindingPeriod":9,"features":"features","addonFee":7.061401241503109,"maximumGiveAwayRestAmount":4.145608029883936,"perVisitPrice":7.457744773683766,"packageName":"packageName","instructionsToGymUsers":"instructionsToGymUsers","availableGyms":[{"gymId":1,"gymName":"gymName","externalGymNumber":6,"location":"location"},{"gymId":1,"gymName":"gymName","externalGymNumber":6,"location":"location"}],"createdUser":"createdUser","monthlyFee":7.386281948385884,"nextPackageNumber":1,"isFirstMonthFree":True,"numberOfVisits":1,"serviceFee":4.965218492984954,"freeMonths":2,"registrationFee":1.1730742509559433,"addOns":[{"articleName":"articleName","endOrder":5,"isIncludeServiceInCharge":True,"articleNumber":6,"startOrder":2,"numberOfItems":5.637376656633329,"articleId":0,"articlePrice":1.4658129805029452,"measureUnit":"measureUnit"},{"articleName":"articleName","endOrder":5,"isIncludeServiceInCharge":True,"articleNumber":6,"startOrder":2,"numberOfItems":5.637376656633329,"articleId":0,"articlePrice":1.4658129805029452,"measureUnit":"measureUnit"}],"packageId":6,"isRegistrationFee":True,"isRestAmount":True,"isSponsorPackage":True,"tags":"tags","createdDate":"2000-01-23T04:56:07.000+00:00","instructionsToWebUsers":"instructionsToWebUsers","numberOfInstallments":1,"isAtg":True,"memberCanAddAddOns":True,"modifiedDate":"2000-01-23T04:56:07.000+00:00","memberCanLeaveWithinFreePeriod":True,"applyForAllGyms":True,"shownInWeb":True,"startDate":"2000-01-23T04:56:07.000+00:00"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/Package',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_package_search(client):
    """Test case for package_search

    Search packages             
    """
    params = [('searchText', 'search_text_example'),
                    ('gymId', -1),
                    ('type', 'all'),
                    ('orderBy', '1'),
                    ('limit', 100),
                    ('offset', 0),
                    ('activeStatus', 1),
                    ('categoryId', -1),
                    ('startpPrice', 0),
                    ('endPrice', 9999999),
                    ('requestSource', 1)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/Package/Search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_package_update_status(client):
    """Test case for package_update_status

    Status update of existing package 
    """
    params = [('packageId', 56),
                    ('status', 1),
                    ('userName', 'system')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/Package/UpdateStatus',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

