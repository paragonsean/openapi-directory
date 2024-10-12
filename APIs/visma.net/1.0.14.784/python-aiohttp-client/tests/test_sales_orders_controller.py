# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.add_sales_order_lines_command import AddSalesOrderLinesCommand
from openapi_server.models.new_sales_order_command import NewSalesOrderCommand
from openapi_server.models.patch_sales_order_command import PatchSalesOrderCommand
from openapi_server.models.patch_sales_order_lines_command import PatchSalesOrderLinesCommand
from openapi_server.models.problem_details import ProblemDetails
from openapi_server.models.sales_order_commission_dto import SalesOrderCommissionDto
from openapi_server.models.sales_order_discount_dto import SalesOrderDiscountDto
from openapi_server.models.sales_order_dto import SalesOrderDto
from openapi_server.models.sales_order_expansions import SalesOrderExpansions
from openapi_server.models.sales_order_line_dto import SalesOrderLineDto
from openapi_server.models.sales_order_line_dto_paged_result import SalesOrderLineDtoPagedResult
from openapi_server.models.sales_order_list_dto_paged_result import SalesOrderListDtoPagedResult
from openapi_server.models.sales_order_rot_rut_dto import SalesOrderRotRutDto
from openapi_server.models.sales_order_shipment_dto import SalesOrderShipmentDto
from openapi_server.models.sales_order_tax_dto import SalesOrderTaxDto
from openapi_server.models.sales_order_validation_problem_details import SalesOrderValidationProblemDetails


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_sales_orders_add_lines_typeorder_idlines(client):
    """Test case for sales_orders_add_lines_typeorder_idlines

    Adds new lines to a existing sales order in the system
    """
    body = {"lines":[{"note":"note","salesAccountId":"salesAccountId","hasManualDiscount":True,"supplierId":"supplierId","externalLink":"externalLink","warehouseLocationId":"warehouseLocationId","description":"description","discountAmount":5.962133916683182,"hasManualPrice":True,"requestDate":"2000-01-23T04:56:07.000+00:00","reasonCode":"reasonCode","salesPersonId":"salesPersonId","unitPrice":4.145608029883936,"branchId":"branchId","discountPercent":12.747533132666561,"quantity":7.061401241503109,"unitOfMeasure":"unitOfMeasure","subaccount":{"key":"subaccount"},"shipDate":"2000-01-23T04:56:07.000+00:00","supplierPrice":9.301444243932576,"purchaseOrderSource":"purchaseOrderSource","projectTaskId":"projectTaskId","discountCode":"discountCode","undershipThreshold":36.160767492519106,"commissionable":True,"shippingRule":"shippingRule","warehouseId":"warehouseId","unitCost":2.027123023002322,"inventoryId":"inventoryId","overshipThreshold":306.9620162354354,"operation":"operation","taxCategoryId":"taxCategoryId"},{"note":"note","salesAccountId":"salesAccountId","hasManualDiscount":True,"supplierId":"supplierId","externalLink":"externalLink","warehouseLocationId":"warehouseLocationId","description":"description","discountAmount":5.962133916683182,"hasManualPrice":True,"requestDate":"2000-01-23T04:56:07.000+00:00","reasonCode":"reasonCode","salesPersonId":"salesPersonId","unitPrice":4.145608029883936,"branchId":"branchId","discountPercent":12.747533132666561,"quantity":7.061401241503109,"unitOfMeasure":"unitOfMeasure","subaccount":{"key":"subaccount"},"shipDate":"2000-01-23T04:56:07.000+00:00","supplierPrice":9.301444243932576,"purchaseOrderSource":"purchaseOrderSource","projectTaskId":"projectTaskId","discountCode":"discountCode","undershipThreshold":36.160767492519106,"commissionable":True,"shippingRule":"shippingRule","warehouseId":"warehouseId","unitCost":2.027123023002322,"inventoryId":"inventoryId","overshipThreshold":306.9620162354354,"operation":"operation","taxCategoryId":"taxCategoryId"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/SalesOrders/{type}/{order_id}/lines'.format(type='type_example', order_id='order_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_sales_orders_create_new_item(client):
    """Test case for sales_orders_create_new_item

    Adds a new sales order to the system
    """
    body = {"date":"2000-01-23T04:56:07.000+00:00","note":"note","orderId":"orderId","freight":{"premiumAmount":1.4658129805029452,"cost":6.027456183070403,"taxCategoryId":"taxCategoryId"},"paymentSettings":{"paymentMethodId":"paymentMethodId","paymentReference":"paymentReference","cashAccountId":"cashAccountId"},"description":"description","ownerId":"ownerId","type":"type","useReplacementCostForMarginAndProfit":True,"billing":{"address":{"city":"city","postalCode":"postalCode","stateId":"stateId","line3":"line3","line2":"line2","countryId":"countryId","line1":"line1"},"contact":{"name":"name","attention":"attention","email":"email","phone1":"phone1"}},"taxZoneId":"taxZoneId","requestOn":"2000-01-23T04:56:07.000+00:00","orderLines":[{"note":"note","salesAccountId":"salesAccountId","hasManualDiscount":True,"supplierId":"supplierId","externalLink":"externalLink","warehouseLocationId":"warehouseLocationId","description":"description","discountAmount":5.962133916683182,"hasManualPrice":True,"requestDate":"2000-01-23T04:56:07.000+00:00","reasonCode":"reasonCode","salesPersonId":"salesPersonId","unitPrice":4.145608029883936,"branchId":"branchId","discountPercent":12.747533132666561,"quantity":7.061401241503109,"unitOfMeasure":"unitOfMeasure","subaccount":{"key":"subaccount"},"shipDate":"2000-01-23T04:56:07.000+00:00","supplierPrice":9.301444243932576,"purchaseOrderSource":"purchaseOrderSource","projectTaskId":"projectTaskId","discountCode":"discountCode","undershipThreshold":36.160767492519106,"commissionable":True,"shippingRule":"shippingRule","warehouseId":"warehouseId","unitCost":2.027123023002322,"inventoryId":"inventoryId","overshipThreshold":306.9620162354354,"operation":"operation","taxCategoryId":"taxCategoryId"},{"note":"note","salesAccountId":"salesAccountId","hasManualDiscount":True,"supplierId":"supplierId","externalLink":"externalLink","warehouseLocationId":"warehouseLocationId","description":"description","discountAmount":5.962133916683182,"hasManualPrice":True,"requestDate":"2000-01-23T04:56:07.000+00:00","reasonCode":"reasonCode","salesPersonId":"salesPersonId","unitPrice":4.145608029883936,"branchId":"branchId","discountPercent":12.747533132666561,"quantity":7.061401241503109,"unitOfMeasure":"unitOfMeasure","subaccount":{"key":"subaccount"},"shipDate":"2000-01-23T04:56:07.000+00:00","supplierPrice":9.301444243932576,"purchaseOrderSource":"purchaseOrderSource","projectTaskId":"projectTaskId","discountCode":"discountCode","undershipThreshold":36.160767492519106,"commissionable":True,"shippingRule":"shippingRule","warehouseId":"warehouseId","unitCost":2.027123023002322,"inventoryId":"inventoryId","overshipThreshold":306.9620162354354,"operation":"operation","taxCategoryId":"taxCategoryId"}],"originalOrderId":"originalOrderId","shipping":{"insurance":True,"shipSeparately":True,"address":{"city":"city","postalCode":"postalCode","stateId":"stateId","line3":"line3","line2":"line2","countryId":"countryId","line1":"line1"},"termsId":"termsId","preferredWarehouseId":"preferredWarehouseId","fobPointId":"fobPointId","rule":"rule","scheduledDate":"2000-01-23T04:56:07.000+00:00","intrastatTransactionTypeId":7,"priority":1,"saturdayDelivery":True,"contact":{"name":"name","attention":"attention","email":"email","phone1":"phone1"},"residentialDelivery":True,"zoneId":"zoneId","shipViaId":"shipViaId"},"cancelBy":"2000-01-23T04:56:07.000+00:00","currencyId":"currencyId","salesPersonId":"salesPersonId","branchId":"branchId","financialInformation":{"postPeriod":"postPeriod","dueDate":"2000-01-23T04:56:07.000+00:00","invoiceId":"invoiceId","invoiceSeparately":True,"invoiceDate":"2000-01-23T04:56:07.000+00:00","cashDiscountDate":"2000-01-23T04:56:07.000+00:00"},"print":{"noteOnExternalDocuments":True,"descriptionOnInvoice":True,"noteOnInternalDocuments":True},"projectId":"projectId","customer":{"refNo":"refNo","termsId":"termsId","contactId":0,"locationId":"locationId","gln":"gln","id":"id","order":"order"},"originalOrderType":"originalOrderType","status":"status"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/SalesOrders',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sales_orders_delete_lines_typeorder_idlines(client):
    """Test case for sales_orders_delete_lines_typeorder_idlines

    Delete lines from an existing sales order
    """
    params = [('ids', [56])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/SalesOrders/{type}/{order_id}/lines'.format(type='type_example', order_id='order_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sales_orders_delete_typeorder_id(client):
    """Test case for sales_orders_delete_typeorder_id

    Delete an existing sales order
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/SalesOrders/{type}/{order_id}'.format(type='type_example', order_id='order_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sales_orders_get_item_async_typeorder_id(client):
    """Test case for sales_orders_get_item_async_typeorder_id

    Gets information about a single sales order
    """
    params = [('expand', [openapi_server.SalesOrderExpansions()])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/SalesOrders/{type}/{order_id}'.format(type='type_example', order_id='order_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sales_orders_get_item_commissions_typeorder_idcommissions(client):
    """Test case for sales_orders_get_item_commissions_typeorder_idcommissions

    Gets commission information for a single sales order
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/SalesOrders/{type}/{order_id}/commissions'.format(type='type_example', order_id='order_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sales_orders_get_item_discounts_typeorder_iddiscounts(client):
    """Test case for sales_orders_get_item_discounts_typeorder_iddiscounts

    Gets discount details information for a single sales order
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/SalesOrders/{type}/{order_id}/discounts'.format(type='type_example', order_id='order_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sales_orders_get_item_line_typeorder_idlinesline_id(client):
    """Test case for sales_orders_get_item_line_typeorder_idlinesline_id

    Gets a specific sales order line for a single sales order
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/SalesOrders/{type}/{order_id}/lines/{line_id}'.format(type='type_example', order_id='order_id_example', line_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sales_orders_get_item_lines_typeorder_idlines(client):
    """Test case for sales_orders_get_item_lines_typeorder_idlines

    Gets sales order lines for a single sales order
    """
    params = [('pageSize', 1000),
                    ('pageIndex', 0)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/SalesOrders/{type}/{order_id}/lines'.format(type='type_example', order_id='order_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sales_orders_get_item_rot_rut_typeorder_idrotrut(client):
    """Test case for sales_orders_get_item_rot_rut_typeorder_idrotrut

    Gets ROT/RUT information for a single sales order
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/SalesOrders/{type}/{order_id}/rotrut'.format(type='type_example', order_id='order_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sales_orders_get_item_tax_typeorder_idtax(client):
    """Test case for sales_orders_get_item_tax_typeorder_idtax

    Gets tax information for a single sales order
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/SalesOrders/{type}/{order_id}/tax'.format(type='type_example', order_id='order_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sales_orders_get_list(client):
    """Test case for sales_orders_get_list

    Gets a paged list with sales orders of any type
    """
    params = [('customerId', 'customer_id_example'),
                    ('status', 'status_example'),
                    ('modifiedSince', '2013-10-20T19:20:30+01:00'),
                    ('pageSize', 100),
                    ('pageIndex', 0),
                    ('orderBy', 'order_by_example'),
                    ('filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/SalesOrders',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sales_orders_get_list_type(client):
    """Test case for sales_orders_get_list_type

    Gets a paged list with sales orders of a specific type
    """
    params = [('customerId', 'customer_id_example'),
                    ('status', 'status_example'),
                    ('modifiedSince', '2013-10-20T19:20:30+01:00'),
                    ('pageSize', 100),
                    ('pageIndex', 0),
                    ('orderBy', 'order_by_example'),
                    ('filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/SalesOrders/{type}'.format(type='type_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sales_orders_get_sales_order_shipment_typeorder_idshipment(client):
    """Test case for sales_orders_get_sales_order_shipment_typeorder_idshipment

    Gets shipment information for a single sales order
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/SalesOrders/{type}/{order_id}/shipment'.format(type='type_example', order_id='order_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_sales_orders_patch_lines_typeorder_idlines(client):
    """Test case for sales_orders_patch_lines_typeorder_idlines

    Make modifications to an existing sales order lines
    """
    body = {"lines":[{"note":"note","salesAccountId":"salesAccountId","hasManualDiscount":True,"supplierId":"supplierId","externalLink":"externalLink","warehouseLocationId":"warehouseLocationId","description":"description","discountAmount":0.8008281904610115,"hasManualPrice":True,"requestDate":"2000-01-23T04:56:07.000+00:00","reasonCode":"reasonCode","salesPersonId":"salesPersonId","unitPrice":2.027123023002322,"branchId":"branchId","discountPercent":20.54912366140806,"quantity":5.637376656633329,"unitOfMeasure":"unitOfMeasure","subaccount":{"key":"subaccount"},"lineId":1,"shipDate":"2000-01-23T04:56:07.000+00:00","supplierPrice":7.061401241503109,"purchaseOrderSource":"purchaseOrderSource","projectTaskId":"projectTaskId","discountCode":"discountCode","undershipThreshold":93.01444243932576,"commissionable":True,"shippingRule":"shippingRule","warehouseId":"warehouseId","sortOrder":2,"unitCost":3.616076749251911,"overshipThreshold":635.9958391098181,"operation":"operation","taxCategoryId":"taxCategoryId"},{"note":"note","salesAccountId":"salesAccountId","hasManualDiscount":True,"supplierId":"supplierId","externalLink":"externalLink","warehouseLocationId":"warehouseLocationId","description":"description","discountAmount":0.8008281904610115,"hasManualPrice":True,"requestDate":"2000-01-23T04:56:07.000+00:00","reasonCode":"reasonCode","salesPersonId":"salesPersonId","unitPrice":2.027123023002322,"branchId":"branchId","discountPercent":20.54912366140806,"quantity":5.637376656633329,"unitOfMeasure":"unitOfMeasure","subaccount":{"key":"subaccount"},"lineId":1,"shipDate":"2000-01-23T04:56:07.000+00:00","supplierPrice":7.061401241503109,"purchaseOrderSource":"purchaseOrderSource","projectTaskId":"projectTaskId","discountCode":"discountCode","undershipThreshold":93.01444243932576,"commissionable":True,"shippingRule":"shippingRule","warehouseId":"warehouseId","sortOrder":2,"unitCost":3.616076749251911,"overshipThreshold":635.9958391098181,"operation":"operation","taxCategoryId":"taxCategoryId"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/SalesOrders/{type}/{order_id}/lines'.format(type='type_example', order_id='order_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_sales_orders_patch_typeorder_id(client):
    """Test case for sales_orders_patch_typeorder_id

    Make modifications to an existing sales order
    """
    body = {"date":"2000-01-23T04:56:07.000+00:00","branchId":"branchId","note":"note","financialInformation":{"postPeriod":"postPeriod","dueDate":"2000-01-23T04:56:07.000+00:00","invoiceId":"invoiceId","invoiceSeparately":True,"invoiceDate":"2000-01-23T04:56:07.000+00:00","cashDiscountDate":"2000-01-23T04:56:07.000+00:00"},"freight":{"premiumAmount":1.4658129805029452,"cost":6.027456183070403,"taxCategoryId":"taxCategoryId"},"paymentSettings":{"paymentMethodId":"paymentMethodId","paymentReference":"paymentReference","cashAccountId":"cashAccountId"},"description":"description","ownerId":"ownerId","useReplacementCostForMarginAndProfit":True,"billing":{"address":{"overridesDefault":True,"city":"city","postalCode":"postalCode","stateId":"stateId","line3":"line3","line2":"line2","countryId":"countryId","line1":"line1"},"contact":{"overridesDefault":True,"name":"name","attention":"attention","email":"email","phone1":"phone1"}},"taxZoneId":"taxZoneId","print":{"noteOnExternalDocuments":True,"descriptionOnInvoice":True,"noteOnInternalDocuments":True},"requestOn":"2000-01-23T04:56:07.000+00:00","originalOrderId":"originalOrderId","shipping":{"insurance":True,"shipSeparately":True,"address":{"overridesDefault":True,"city":"city","postalCode":"postalCode","stateId":"stateId","line3":"line3","line2":"line2","countryId":"countryId","line1":"line1"},"termsId":"termsId","preferredWarehouseId":"preferredWarehouseId","fobPointId":"fobPointId","rule":"rule","scheduledDate":"2000-01-23T04:56:07.000+00:00","intrastatTransactionTypeId":5,"priority":5,"saturdayDelivery":True,"contact":{"overridesDefault":True,"name":"name","attention":"attention","email":"email","phone1":"phone1"},"residentialDelivery":True,"zoneId":"zoneId","shipViaId":"shipViaId"},"cancelBy":"2000-01-23T04:56:07.000+00:00","currencyId":"currencyId","projectId":"projectId","customer":{"refNo":"refNo","termsId":"termsId","contactId":0,"locationId":"locationId","id":"id","order":"order"},"originalOrderType":"originalOrderType","salesPersonId":"salesPersonId","status":"status"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/SalesOrders/{type}/{order_id}'.format(type='type_example', order_id='order_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

