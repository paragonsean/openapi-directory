from typing import List, Dict
from aiohttp import web

from openapi_server.models.accept_portfolio_share_input import AcceptPortfolioShareInput
from openapi_server.models.associate_budget_with_resource_input import AssociateBudgetWithResourceInput
from openapi_server.models.associate_principal_with_portfolio_input import AssociatePrincipalWithPortfolioInput
from openapi_server.models.associate_product_with_portfolio_input import AssociateProductWithPortfolioInput
from openapi_server.models.associate_service_action_with_provisioning_artifact_input import AssociateServiceActionWithProvisioningArtifactInput
from openapi_server.models.associate_tag_option_with_resource_input import AssociateTagOptionWithResourceInput
from openapi_server.models.batch_associate_service_action_with_provisioning_artifact_input import BatchAssociateServiceActionWithProvisioningArtifactInput
from openapi_server.models.batch_associate_service_action_with_provisioning_artifact_output import BatchAssociateServiceActionWithProvisioningArtifactOutput
from openapi_server.models.batch_disassociate_service_action_from_provisioning_artifact_input import BatchDisassociateServiceActionFromProvisioningArtifactInput
from openapi_server.models.batch_disassociate_service_action_from_provisioning_artifact_output import BatchDisassociateServiceActionFromProvisioningArtifactOutput
from openapi_server.models.copy_product_input import CopyProductInput
from openapi_server.models.copy_product_output import CopyProductOutput
from openapi_server.models.create_constraint_input import CreateConstraintInput
from openapi_server.models.create_constraint_output import CreateConstraintOutput
from openapi_server.models.create_portfolio_input import CreatePortfolioInput
from openapi_server.models.create_portfolio_output import CreatePortfolioOutput
from openapi_server.models.create_portfolio_share_input import CreatePortfolioShareInput
from openapi_server.models.create_portfolio_share_output import CreatePortfolioShareOutput
from openapi_server.models.create_product_input import CreateProductInput
from openapi_server.models.create_product_output import CreateProductOutput
from openapi_server.models.create_provisioned_product_plan_input import CreateProvisionedProductPlanInput
from openapi_server.models.create_provisioned_product_plan_output import CreateProvisionedProductPlanOutput
from openapi_server.models.create_provisioning_artifact_input import CreateProvisioningArtifactInput
from openapi_server.models.create_provisioning_artifact_output import CreateProvisioningArtifactOutput
from openapi_server.models.create_service_action_input import CreateServiceActionInput
from openapi_server.models.create_service_action_output import CreateServiceActionOutput
from openapi_server.models.create_tag_option_input import CreateTagOptionInput
from openapi_server.models.create_tag_option_output import CreateTagOptionOutput
from openapi_server.models.delete_constraint_input import DeleteConstraintInput
from openapi_server.models.delete_portfolio_input import DeletePortfolioInput
from openapi_server.models.delete_portfolio_share_input import DeletePortfolioShareInput
from openapi_server.models.delete_portfolio_share_output import DeletePortfolioShareOutput
from openapi_server.models.delete_product_input import DeleteProductInput
from openapi_server.models.delete_provisioned_product_plan_input import DeleteProvisionedProductPlanInput
from openapi_server.models.delete_provisioning_artifact_input import DeleteProvisioningArtifactInput
from openapi_server.models.delete_service_action_input import DeleteServiceActionInput
from openapi_server.models.delete_tag_option_input import DeleteTagOptionInput
from openapi_server.models.describe_constraint_input import DescribeConstraintInput
from openapi_server.models.describe_constraint_output import DescribeConstraintOutput
from openapi_server.models.describe_copy_product_status_input import DescribeCopyProductStatusInput
from openapi_server.models.describe_copy_product_status_output import DescribeCopyProductStatusOutput
from openapi_server.models.describe_portfolio_input import DescribePortfolioInput
from openapi_server.models.describe_portfolio_output import DescribePortfolioOutput
from openapi_server.models.describe_portfolio_share_status_input import DescribePortfolioShareStatusInput
from openapi_server.models.describe_portfolio_share_status_output import DescribePortfolioShareStatusOutput
from openapi_server.models.describe_portfolio_shares_input import DescribePortfolioSharesInput
from openapi_server.models.describe_portfolio_shares_output import DescribePortfolioSharesOutput
from openapi_server.models.describe_product_as_admin_input import DescribeProductAsAdminInput
from openapi_server.models.describe_product_as_admin_output import DescribeProductAsAdminOutput
from openapi_server.models.describe_product_input import DescribeProductInput
from openapi_server.models.describe_product_output import DescribeProductOutput
from openapi_server.models.describe_product_view_input import DescribeProductViewInput
from openapi_server.models.describe_product_view_output import DescribeProductViewOutput
from openapi_server.models.describe_provisioned_product_input import DescribeProvisionedProductInput
from openapi_server.models.describe_provisioned_product_output import DescribeProvisionedProductOutput
from openapi_server.models.describe_provisioned_product_plan_input import DescribeProvisionedProductPlanInput
from openapi_server.models.describe_provisioned_product_plan_output import DescribeProvisionedProductPlanOutput
from openapi_server.models.describe_provisioning_artifact_input import DescribeProvisioningArtifactInput
from openapi_server.models.describe_provisioning_artifact_output import DescribeProvisioningArtifactOutput
from openapi_server.models.describe_provisioning_parameters_input import DescribeProvisioningParametersInput
from openapi_server.models.describe_provisioning_parameters_output import DescribeProvisioningParametersOutput
from openapi_server.models.describe_record_input import DescribeRecordInput
from openapi_server.models.describe_record_output import DescribeRecordOutput
from openapi_server.models.describe_service_action_execution_parameters_input import DescribeServiceActionExecutionParametersInput
from openapi_server.models.describe_service_action_execution_parameters_output import DescribeServiceActionExecutionParametersOutput
from openapi_server.models.describe_service_action_input import DescribeServiceActionInput
from openapi_server.models.describe_service_action_output import DescribeServiceActionOutput
from openapi_server.models.describe_tag_option_input import DescribeTagOptionInput
from openapi_server.models.describe_tag_option_output import DescribeTagOptionOutput
from openapi_server.models.disassociate_budget_from_resource_input import DisassociateBudgetFromResourceInput
from openapi_server.models.disassociate_principal_from_portfolio_input import DisassociatePrincipalFromPortfolioInput
from openapi_server.models.disassociate_product_from_portfolio_input import DisassociateProductFromPortfolioInput
from openapi_server.models.disassociate_service_action_from_provisioning_artifact_input import DisassociateServiceActionFromProvisioningArtifactInput
from openapi_server.models.disassociate_tag_option_from_resource_input import DisassociateTagOptionFromResourceInput
from openapi_server.models.execute_provisioned_product_plan_input import ExecuteProvisionedProductPlanInput
from openapi_server.models.execute_provisioned_product_plan_output import ExecuteProvisionedProductPlanOutput
from openapi_server.models.execute_provisioned_product_service_action_input import ExecuteProvisionedProductServiceActionInput
from openapi_server.models.execute_provisioned_product_service_action_output import ExecuteProvisionedProductServiceActionOutput
from openapi_server.models.get_aws_organizations_access_status_output import GetAWSOrganizationsAccessStatusOutput
from openapi_server.models.get_provisioned_product_outputs_input import GetProvisionedProductOutputsInput
from openapi_server.models.get_provisioned_product_outputs_output import GetProvisionedProductOutputsOutput
from openapi_server.models.import_as_provisioned_product_input import ImportAsProvisionedProductInput
from openapi_server.models.import_as_provisioned_product_output import ImportAsProvisionedProductOutput
from openapi_server.models.list_accepted_portfolio_shares_input import ListAcceptedPortfolioSharesInput
from openapi_server.models.list_accepted_portfolio_shares_output import ListAcceptedPortfolioSharesOutput
from openapi_server.models.list_budgets_for_resource_input import ListBudgetsForResourceInput
from openapi_server.models.list_budgets_for_resource_output import ListBudgetsForResourceOutput
from openapi_server.models.list_constraints_for_portfolio_input import ListConstraintsForPortfolioInput
from openapi_server.models.list_constraints_for_portfolio_output import ListConstraintsForPortfolioOutput
from openapi_server.models.list_launch_paths_input import ListLaunchPathsInput
from openapi_server.models.list_launch_paths_output import ListLaunchPathsOutput
from openapi_server.models.list_organization_portfolio_access_input import ListOrganizationPortfolioAccessInput
from openapi_server.models.list_organization_portfolio_access_output import ListOrganizationPortfolioAccessOutput
from openapi_server.models.list_portfolio_access_input import ListPortfolioAccessInput
from openapi_server.models.list_portfolio_access_output import ListPortfolioAccessOutput
from openapi_server.models.list_portfolios_for_product_input import ListPortfoliosForProductInput
from openapi_server.models.list_portfolios_for_product_output import ListPortfoliosForProductOutput
from openapi_server.models.list_portfolios_input import ListPortfoliosInput
from openapi_server.models.list_portfolios_output import ListPortfoliosOutput
from openapi_server.models.list_principals_for_portfolio_input import ListPrincipalsForPortfolioInput
from openapi_server.models.list_principals_for_portfolio_output import ListPrincipalsForPortfolioOutput
from openapi_server.models.list_provisioned_product_plans_input import ListProvisionedProductPlansInput
from openapi_server.models.list_provisioned_product_plans_output import ListProvisionedProductPlansOutput
from openapi_server.models.list_provisioning_artifacts_for_service_action_input import ListProvisioningArtifactsForServiceActionInput
from openapi_server.models.list_provisioning_artifacts_for_service_action_output import ListProvisioningArtifactsForServiceActionOutput
from openapi_server.models.list_provisioning_artifacts_input import ListProvisioningArtifactsInput
from openapi_server.models.list_provisioning_artifacts_output import ListProvisioningArtifactsOutput
from openapi_server.models.list_record_history_input import ListRecordHistoryInput
from openapi_server.models.list_record_history_output import ListRecordHistoryOutput
from openapi_server.models.list_resources_for_tag_option_input import ListResourcesForTagOptionInput
from openapi_server.models.list_resources_for_tag_option_output import ListResourcesForTagOptionOutput
from openapi_server.models.list_service_actions_for_provisioning_artifact_input import ListServiceActionsForProvisioningArtifactInput
from openapi_server.models.list_service_actions_for_provisioning_artifact_output import ListServiceActionsForProvisioningArtifactOutput
from openapi_server.models.list_service_actions_input import ListServiceActionsInput
from openapi_server.models.list_service_actions_output import ListServiceActionsOutput
from openapi_server.models.list_stack_instances_for_provisioned_product_input import ListStackInstancesForProvisionedProductInput
from openapi_server.models.list_stack_instances_for_provisioned_product_output import ListStackInstancesForProvisionedProductOutput
from openapi_server.models.list_tag_options_input import ListTagOptionsInput
from openapi_server.models.list_tag_options_output import ListTagOptionsOutput
from openapi_server.models.notify_provision_product_engine_workflow_result_input import NotifyProvisionProductEngineWorkflowResultInput
from openapi_server.models.notify_terminate_provisioned_product_engine_workflow_result_input import NotifyTerminateProvisionedProductEngineWorkflowResultInput
from openapi_server.models.notify_update_provisioned_product_engine_workflow_result_input import NotifyUpdateProvisionedProductEngineWorkflowResultInput
from openapi_server.models.provision_product_input import ProvisionProductInput
from openapi_server.models.provision_product_output import ProvisionProductOutput
from openapi_server.models.reject_portfolio_share_input import RejectPortfolioShareInput
from openapi_server.models.scan_provisioned_products_input import ScanProvisionedProductsInput
from openapi_server.models.scan_provisioned_products_output import ScanProvisionedProductsOutput
from openapi_server.models.search_products_as_admin_input import SearchProductsAsAdminInput
from openapi_server.models.search_products_as_admin_output import SearchProductsAsAdminOutput
from openapi_server.models.search_products_input import SearchProductsInput
from openapi_server.models.search_products_output import SearchProductsOutput
from openapi_server.models.search_provisioned_products_input import SearchProvisionedProductsInput
from openapi_server.models.search_provisioned_products_output import SearchProvisionedProductsOutput
from openapi_server.models.terminate_provisioned_product_input import TerminateProvisionedProductInput
from openapi_server.models.terminate_provisioned_product_output import TerminateProvisionedProductOutput
from openapi_server.models.update_constraint_input import UpdateConstraintInput
from openapi_server.models.update_constraint_output import UpdateConstraintOutput
from openapi_server.models.update_portfolio_input import UpdatePortfolioInput
from openapi_server.models.update_portfolio_output import UpdatePortfolioOutput
from openapi_server.models.update_portfolio_share_input import UpdatePortfolioShareInput
from openapi_server.models.update_portfolio_share_output import UpdatePortfolioShareOutput
from openapi_server.models.update_product_input import UpdateProductInput
from openapi_server.models.update_product_output import UpdateProductOutput
from openapi_server.models.update_provisioned_product_input import UpdateProvisionedProductInput
from openapi_server.models.update_provisioned_product_output import UpdateProvisionedProductOutput
from openapi_server.models.update_provisioned_product_properties_input import UpdateProvisionedProductPropertiesInput
from openapi_server.models.update_provisioned_product_properties_output import UpdateProvisionedProductPropertiesOutput
from openapi_server.models.update_provisioning_artifact_input import UpdateProvisioningArtifactInput
from openapi_server.models.update_provisioning_artifact_output import UpdateProvisioningArtifactOutput
from openapi_server.models.update_service_action_input import UpdateServiceActionInput
from openapi_server.models.update_service_action_output import UpdateServiceActionOutput
from openapi_server.models.update_tag_option_input import UpdateTagOptionInput
from openapi_server.models.update_tag_option_output import UpdateTagOptionOutput
from openapi_server import util


async def accept_portfolio_share(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """accept_portfolio_share

    Accepts an offer to share the specified portfolio.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = AcceptPortfolioShareInput.from_dict(body)
    return web.Response(status=200)


async def associate_budget_with_resource(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """associate_budget_with_resource

    Associates the specified budget with the specified resource.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = AssociateBudgetWithResourceInput.from_dict(body)
    return web.Response(status=200)


async def associate_principal_with_portfolio(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """associate_principal_with_portfolio

    &lt;p&gt;Associates the specified principal ARN with the specified portfolio.&lt;/p&gt; &lt;p&gt;If you share the portfolio with principal name sharing enabled, the &lt;code&gt;PrincipalARN&lt;/code&gt; association is included in the share. &lt;/p&gt; &lt;p&gt;The &lt;code&gt;PortfolioID&lt;/code&gt;, &lt;code&gt;PrincipalARN&lt;/code&gt;, and &lt;code&gt;PrincipalType&lt;/code&gt; parameters are required. &lt;/p&gt; &lt;p&gt;You can associate a maximum of 10 Principals with a portfolio using &lt;code&gt;PrincipalType&lt;/code&gt; as &lt;code&gt;IAM_PATTERN&lt;/code&gt; &lt;/p&gt; &lt;note&gt; &lt;p&gt;When you associate a principal with portfolio, a potential privilege escalation path may occur when that portfolio is then shared with other accounts. For a user in a recipient account who is &lt;i&gt;not&lt;/i&gt; an Service Catalog Admin, but still has the ability to create Principals (Users/Groups/Roles), that user could create a role that matches a principal name association for the portfolio. Although this user may not know which principal names are associated through Service Catalog, they may be able to guess the user. If this potential escalation path is a concern, then Service Catalog recommends using &lt;code&gt;PrincipalType&lt;/code&gt; as &lt;code&gt;IAM&lt;/code&gt;. With this configuration, the &lt;code&gt;PrincipalARN&lt;/code&gt; must already exist in the recipient account before it can be associated. &lt;/p&gt; &lt;/note&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = AssociatePrincipalWithPortfolioInput.from_dict(body)
    return web.Response(status=200)


async def associate_product_with_portfolio(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """associate_product_with_portfolio

    &lt;p&gt;Associates the specified product with the specified portfolio.&lt;/p&gt; &lt;p&gt;A delegated admin is authorized to invoke this command.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = AssociateProductWithPortfolioInput.from_dict(body)
    return web.Response(status=200)


async def associate_service_action_with_provisioning_artifact(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """associate_service_action_with_provisioning_artifact

    Associates a self-service action with a provisioning artifact.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = AssociateServiceActionWithProvisioningArtifactInput.from_dict(body)
    return web.Response(status=200)


async def associate_tag_option_with_resource(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """associate_tag_option_with_resource

    Associate the specified TagOption with the specified portfolio or product.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = AssociateTagOptionWithResourceInput.from_dict(body)
    return web.Response(status=200)


async def batch_associate_service_action_with_provisioning_artifact(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """batch_associate_service_action_with_provisioning_artifact

    Associates multiple self-service actions with provisioning artifacts.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = BatchAssociateServiceActionWithProvisioningArtifactInput.from_dict(body)
    return web.Response(status=200)


async def batch_disassociate_service_action_from_provisioning_artifact(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """batch_disassociate_service_action_from_provisioning_artifact

    Disassociates a batch of self-service actions from the specified provisioning artifact.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = BatchDisassociateServiceActionFromProvisioningArtifactInput.from_dict(body)
    return web.Response(status=200)


async def copy_product(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """copy_product

    &lt;p&gt;Copies the specified source product to the specified target product or a new product.&lt;/p&gt; &lt;p&gt;You can copy a product to the same account or another account. You can copy a product to the same Region or another Region. If you copy a product to another account, you must first share the product in a portfolio using &lt;a&gt;CreatePortfolioShare&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;This operation is performed asynchronously. To track the progress of the operation, use &lt;a&gt;DescribeCopyProductStatus&lt;/a&gt;.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CopyProductInput.from_dict(body)
    return web.Response(status=200)


async def create_constraint(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_constraint

    &lt;p&gt;Creates a constraint.&lt;/p&gt; &lt;p&gt;A delegated admin is authorized to invoke this command.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateConstraintInput.from_dict(body)
    return web.Response(status=200)


async def create_portfolio(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_portfolio

    &lt;p&gt;Creates a portfolio.&lt;/p&gt; &lt;p&gt;A delegated admin is authorized to invoke this command.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreatePortfolioInput.from_dict(body)
    return web.Response(status=200)


async def create_portfolio_share(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_portfolio_share

    &lt;p&gt;Shares the specified portfolio with the specified account or organization node. Shares to an organization node can only be created by the management account of an organization or by a delegated administrator. You can share portfolios to an organization, an organizational unit, or a specific account.&lt;/p&gt; &lt;p&gt;Note that if a delegated admin is de-registered, they can no longer create portfolio shares.&lt;/p&gt; &lt;p&gt; &lt;code&gt;AWSOrganizationsAccess&lt;/code&gt; must be enabled in order to create a portfolio share to an organization node.&lt;/p&gt; &lt;p&gt;You can&#39;t share a shared resource, including portfolios that contain a shared product.&lt;/p&gt; &lt;p&gt;If the portfolio share with the specified account or organization node already exists, this action will have no effect and will not return an error. To update an existing share, you must use the &lt;code&gt; UpdatePortfolioShare&lt;/code&gt; API instead. &lt;/p&gt; &lt;note&gt; &lt;p&gt;When you associate a principal with portfolio, a potential privilege escalation path may occur when that portfolio is then shared with other accounts. For a user in a recipient account who is &lt;i&gt;not&lt;/i&gt; an Service Catalog Admin, but still has the ability to create Principals (Users/Groups/Roles), that user could create a role that matches a principal name association for the portfolio. Although this user may not know which principal names are associated through Service Catalog, they may be able to guess the user. If this potential escalation path is a concern, then Service Catalog recommends using &lt;code&gt;PrincipalType&lt;/code&gt; as &lt;code&gt;IAM&lt;/code&gt;. With this configuration, the &lt;code&gt;PrincipalARN&lt;/code&gt; must already exist in the recipient account before it can be associated. &lt;/p&gt; &lt;/note&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreatePortfolioShareInput.from_dict(body)
    return web.Response(status=200)


async def create_product(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_product

    &lt;p&gt;Creates a product.&lt;/p&gt; &lt;p&gt;A delegated admin is authorized to invoke this command.&lt;/p&gt; &lt;p&gt;The user or role that performs this operation must have the &lt;code&gt;cloudformation:GetTemplate&lt;/code&gt; IAM policy permission. This policy permission is required when using the &lt;code&gt;ImportFromPhysicalId&lt;/code&gt; template source in the information data section.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateProductInput.from_dict(body)
    return web.Response(status=200)


async def create_provisioned_product_plan(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_provisioned_product_plan

    &lt;p&gt;Creates a plan.&lt;/p&gt; &lt;p&gt;A plan includes the list of resources to be created (when provisioning a new product) or modified (when updating a provisioned product) when the plan is executed.&lt;/p&gt; &lt;p&gt;You can create one plan for each provisioned product. To create a plan for an existing provisioned product, the product status must be AVAILABLE or TAINTED.&lt;/p&gt; &lt;p&gt;To view the resource changes in the change set, use &lt;a&gt;DescribeProvisionedProductPlan&lt;/a&gt;. To create or modify the provisioned product, use &lt;a&gt;ExecuteProvisionedProductPlan&lt;/a&gt;.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateProvisionedProductPlanInput.from_dict(body)
    return web.Response(status=200)


async def create_provisioning_artifact(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_provisioning_artifact

    &lt;p&gt;Creates a provisioning artifact (also known as a version) for the specified product.&lt;/p&gt; &lt;p&gt;You cannot create a provisioning artifact for a product that was shared with you.&lt;/p&gt; &lt;p&gt;The user or role that performs this operation must have the &lt;code&gt;cloudformation:GetTemplate&lt;/code&gt; IAM policy permission. This policy permission is required when using the &lt;code&gt;ImportFromPhysicalId&lt;/code&gt; template source in the information data section.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateProvisioningArtifactInput.from_dict(body)
    return web.Response(status=200)


async def create_service_action(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_service_action

    Creates a self-service action.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateServiceActionInput.from_dict(body)
    return web.Response(status=200)


async def create_tag_option(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_tag_option

    Creates a TagOption.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateTagOptionInput.from_dict(body)
    return web.Response(status=200)


async def delete_constraint(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_constraint

    &lt;p&gt;Deletes the specified constraint.&lt;/p&gt; &lt;p&gt;A delegated admin is authorized to invoke this command.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DeleteConstraintInput.from_dict(body)
    return web.Response(status=200)


async def delete_portfolio(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_portfolio

    &lt;p&gt;Deletes the specified portfolio.&lt;/p&gt; &lt;p&gt;You cannot delete a portfolio if it was shared with you or if it has associated products, users, constraints, or shared accounts.&lt;/p&gt; &lt;p&gt;A delegated admin is authorized to invoke this command.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DeletePortfolioInput.from_dict(body)
    return web.Response(status=200)


async def delete_portfolio_share(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_portfolio_share

    &lt;p&gt;Stops sharing the specified portfolio with the specified account or organization node. Shares to an organization node can only be deleted by the management account of an organization or by a delegated administrator.&lt;/p&gt; &lt;p&gt;Note that if a delegated admin is de-registered, portfolio shares created from that account are removed.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DeletePortfolioShareInput.from_dict(body)
    return web.Response(status=200)


async def delete_product(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_product

    &lt;p&gt;Deletes the specified product.&lt;/p&gt; &lt;p&gt;You cannot delete a product if it was shared with you or is associated with a portfolio.&lt;/p&gt; &lt;p&gt;A delegated admin is authorized to invoke this command.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DeleteProductInput.from_dict(body)
    return web.Response(status=200)


async def delete_provisioned_product_plan(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_provisioned_product_plan

    Deletes the specified plan.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DeleteProvisionedProductPlanInput.from_dict(body)
    return web.Response(status=200)


async def delete_provisioning_artifact(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_provisioning_artifact

    &lt;p&gt;Deletes the specified provisioning artifact (also known as a version) for the specified product.&lt;/p&gt; &lt;p&gt;You cannot delete a provisioning artifact associated with a product that was shared with you. You cannot delete the last provisioning artifact for a product, because a product must have at least one provisioning artifact.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DeleteProvisioningArtifactInput.from_dict(body)
    return web.Response(status=200)


async def delete_service_action(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_service_action

    Deletes a self-service action.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DeleteServiceActionInput.from_dict(body)
    return web.Response(status=200)


async def delete_tag_option(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_tag_option

    &lt;p&gt;Deletes the specified TagOption.&lt;/p&gt; &lt;p&gt;You cannot delete a TagOption if it is associated with a product or portfolio.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DeleteTagOptionInput.from_dict(body)
    return web.Response(status=200)


async def describe_constraint(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_constraint

    Gets information about the specified constraint.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DescribeConstraintInput.from_dict(body)
    return web.Response(status=200)


async def describe_copy_product_status(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_copy_product_status

    Gets the status of the specified copy product operation.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DescribeCopyProductStatusInput.from_dict(body)
    return web.Response(status=200)


async def describe_portfolio(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_portfolio

    &lt;p&gt;Gets information about the specified portfolio.&lt;/p&gt; &lt;p&gt;A delegated admin is authorized to invoke this command.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DescribePortfolioInput.from_dict(body)
    return web.Response(status=200)


async def describe_portfolio_share_status(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_portfolio_share_status

    Gets the status of the specified portfolio share operation. This API can only be called by the management account in the organization or by a delegated admin.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DescribePortfolioShareStatusInput.from_dict(body)
    return web.Response(status=200)


async def describe_portfolio_shares(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, page_size=None, page_token=None) -> web.Response:
    """describe_portfolio_shares

    &lt;p&gt;Returns a summary of each of the portfolio shares that were created for the specified portfolio.&lt;/p&gt; &lt;p&gt;You can use this API to determine which accounts or organizational nodes this portfolio have been shared, whether the recipient entity has imported the share, and whether TagOptions are included with the share.&lt;/p&gt; &lt;p&gt;The &lt;code&gt;PortfolioId&lt;/code&gt; and &lt;code&gt;Type&lt;/code&gt; parameters are both required.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param page_size: Pagination limit
    :type page_size: str
    :param page_token: Pagination token
    :type page_token: str

    """
    body = DescribePortfolioSharesInput.from_dict(body)
    return web.Response(status=200)


async def describe_product(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_product

    &lt;p&gt;Gets information about the specified product.&lt;/p&gt; &lt;note&gt; &lt;p&gt; Running this operation with administrator access results in a failure. &lt;a&gt;DescribeProductAsAdmin&lt;/a&gt; should be used instead. &lt;/p&gt; &lt;/note&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DescribeProductInput.from_dict(body)
    return web.Response(status=200)


async def describe_product_as_admin(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_product_as_admin

    Gets information about the specified product. This operation is run with administrator access.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DescribeProductAsAdminInput.from_dict(body)
    return web.Response(status=200)


async def describe_product_view(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_product_view

    Gets information about the specified product.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DescribeProductViewInput.from_dict(body)
    return web.Response(status=200)


async def describe_provisioned_product(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_provisioned_product

    Gets information about the specified provisioned product.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DescribeProvisionedProductInput.from_dict(body)
    return web.Response(status=200)


async def describe_provisioned_product_plan(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_provisioned_product_plan

    Gets information about the resource changes for the specified plan.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DescribeProvisionedProductPlanInput.from_dict(body)
    return web.Response(status=200)


async def describe_provisioning_artifact(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_provisioning_artifact

    Gets information about the specified provisioning artifact (also known as a version) for the specified product.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DescribeProvisioningArtifactInput.from_dict(body)
    return web.Response(status=200)


async def describe_provisioning_parameters(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_provisioning_parameters

    &lt;p&gt;Gets information about the configuration required to provision the specified product using the specified provisioning artifact.&lt;/p&gt; &lt;p&gt;If the output contains a TagOption key with an empty list of values, there is a TagOption conflict for that key. The end user cannot take action to fix the conflict, and launch is not blocked. In subsequent calls to &lt;a&gt;ProvisionProduct&lt;/a&gt;, do not include conflicted TagOption keys as tags, or this causes the error \&quot;Parameter validation failed: Missing required parameter in Tags[&lt;i&gt;N&lt;/i&gt;]:&lt;i&gt;Value&lt;/i&gt;\&quot;. Tag the provisioned product with the value &lt;code&gt;sc-tagoption-conflict-portfolioId-productId&lt;/code&gt;.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DescribeProvisioningParametersInput.from_dict(body)
    return web.Response(status=200)


async def describe_record(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_record

    &lt;p&gt;Gets information about the specified request operation.&lt;/p&gt; &lt;p&gt;Use this operation after calling a request operation (for example, &lt;a&gt;ProvisionProduct&lt;/a&gt;, &lt;a&gt;TerminateProvisionedProduct&lt;/a&gt;, or &lt;a&gt;UpdateProvisionedProduct&lt;/a&gt;). &lt;/p&gt; &lt;note&gt; &lt;p&gt;If a provisioned product was transferred to a new owner using &lt;a&gt;UpdateProvisionedProductProperties&lt;/a&gt;, the new owner will be able to describe all past records for that product. The previous owner will no longer be able to describe the records, but will be able to use &lt;a&gt;ListRecordHistory&lt;/a&gt; to see the product&#39;s history from when he was the owner.&lt;/p&gt; &lt;/note&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DescribeRecordInput.from_dict(body)
    return web.Response(status=200)


async def describe_service_action(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_service_action

    Describes a self-service action.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DescribeServiceActionInput.from_dict(body)
    return web.Response(status=200)


async def describe_service_action_execution_parameters(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_service_action_execution_parameters

    Finds the default parameters for a specific self-service action on a specific provisioned product and returns a map of the results to the user.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DescribeServiceActionExecutionParametersInput.from_dict(body)
    return web.Response(status=200)


async def describe_tag_option(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_tag_option

    Gets information about the specified TagOption.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DescribeTagOptionInput.from_dict(body)
    return web.Response(status=200)


async def disable_aws_organizations_access(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """disable_aws_organizations_access

    &lt;p&gt;Disable portfolio sharing through the Organizations service. This command will not delete your current shares, but prevents you from creating new shares throughout your organization. Current shares are not kept in sync with your organization structure if the structure changes after calling this API. Only the management account in the organization can call this API.&lt;/p&gt; &lt;p&gt;You cannot call this API if there are active delegated administrators in the organization.&lt;/p&gt; &lt;p&gt;Note that a delegated administrator is not authorized to invoke &lt;code&gt;DisableAWSOrganizationsAccess&lt;/code&gt;.&lt;/p&gt; &lt;important&gt; &lt;p&gt;If you share an Service Catalog portfolio in an organization within Organizations, and then disable Organizations access for Service Catalog, the portfolio access permissions will not sync with the latest changes to the organization structure. Specifically, accounts that you removed from the organization after disabling Service Catalog access will retain access to the previously shared portfolio.&lt;/p&gt; &lt;/important&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: 
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def disassociate_budget_from_resource(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """disassociate_budget_from_resource

    Disassociates the specified budget from the specified resource.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DisassociateBudgetFromResourceInput.from_dict(body)
    return web.Response(status=200)


async def disassociate_principal_from_portfolio(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """disassociate_principal_from_portfolio

    &lt;p&gt;Disassociates a previously associated principal ARN from a specified portfolio.&lt;/p&gt; &lt;p&gt;The &lt;code&gt;PrincipalType&lt;/code&gt; and &lt;code&gt;PrincipalARN&lt;/code&gt; must match the &lt;code&gt;AssociatePrincipalWithPortfolio&lt;/code&gt; call request details. For example, to disassociate an association created with a &lt;code&gt;PrincipalARN&lt;/code&gt; of &lt;code&gt;PrincipalType&lt;/code&gt; IAM you must use the &lt;code&gt;PrincipalType&lt;/code&gt; IAM when calling &lt;code&gt;DisassociatePrincipalFromPortfolio&lt;/code&gt;. &lt;/p&gt; &lt;p&gt;For portfolios that have been shared with principal name sharing enabled: after disassociating a principal, share recipient accounts will no longer be able to provision products in this portfolio using a role matching the name of the associated principal. &lt;/p&gt; &lt;p&gt;For more information, review &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cli/latest/reference/servicecatalog/associate-principal-with-portfolio.html#options\&quot;&gt;associate-principal-with-portfolio&lt;/a&gt; in the Amazon Web Services CLI Command Reference. &lt;/p&gt; &lt;note&gt; &lt;p&gt;If you disassociate a principal from a portfolio, with PrincipalType as &lt;code&gt;IAM&lt;/code&gt;, the same principal will still have access to the portfolio if it matches one of the associated principals of type &lt;code&gt;IAM_PATTERN&lt;/code&gt;. To fully remove access for a principal, verify all the associated Principals of type &lt;code&gt;IAM_PATTERN&lt;/code&gt;, and then ensure you disassociate any &lt;code&gt;IAM_PATTERN&lt;/code&gt; principals that match the principal whose access you are removing.&lt;/p&gt; &lt;/note&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DisassociatePrincipalFromPortfolioInput.from_dict(body)
    return web.Response(status=200)


async def disassociate_product_from_portfolio(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """disassociate_product_from_portfolio

    &lt;p&gt;Disassociates the specified product from the specified portfolio. &lt;/p&gt; &lt;p&gt;A delegated admin is authorized to invoke this command.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DisassociateProductFromPortfolioInput.from_dict(body)
    return web.Response(status=200)


async def disassociate_service_action_from_provisioning_artifact(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """disassociate_service_action_from_provisioning_artifact

    Disassociates the specified self-service action association from the specified provisioning artifact.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DisassociateServiceActionFromProvisioningArtifactInput.from_dict(body)
    return web.Response(status=200)


async def disassociate_tag_option_from_resource(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """disassociate_tag_option_from_resource

    Disassociates the specified TagOption from the specified resource.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DisassociateTagOptionFromResourceInput.from_dict(body)
    return web.Response(status=200)


async def enable_aws_organizations_access(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """enable_aws_organizations_access

    &lt;p&gt;Enable portfolio sharing feature through Organizations. This API will allow Service Catalog to receive updates on your organization in order to sync your shares with the current structure. This API can only be called by the management account in the organization.&lt;/p&gt; &lt;p&gt;When you call this API, Service Catalog calls &lt;code&gt;organizations:EnableAWSServiceAccess&lt;/code&gt; on your behalf so that your shares stay in sync with any changes in your Organizations structure.&lt;/p&gt; &lt;p&gt;Note that a delegated administrator is not authorized to invoke &lt;code&gt;EnableAWSOrganizationsAccess&lt;/code&gt;.&lt;/p&gt; &lt;important&gt; &lt;p&gt;If you have previously disabled Organizations access for Service Catalog, and then enable access again, the portfolio access permissions might not sync with the latest changes to the organization structure. Specifically, accounts that you removed from the organization after disabling Service Catalog access, and before you enabled access again, can retain access to the previously shared portfolio. As a result, an account that has been removed from the organization might still be able to create or manage Amazon Web Services resources when it is no longer authorized to do so. Amazon Web Services is working to resolve this issue.&lt;/p&gt; &lt;/important&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: 
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def execute_provisioned_product_plan(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """execute_provisioned_product_plan

    Provisions or modifies a product based on the resource changes for the specified plan.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = ExecuteProvisionedProductPlanInput.from_dict(body)
    return web.Response(status=200)


async def execute_provisioned_product_service_action(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """execute_provisioned_product_service_action

    Executes a self-service action against a provisioned product.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = ExecuteProvisionedProductServiceActionInput.from_dict(body)
    return web.Response(status=200)


async def get_aws_organizations_access_status(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_aws_organizations_access_status

    Get the Access Status for Organizations portfolio share feature. This API can only be called by the management account in the organization or by a delegated admin.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: 
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def get_provisioned_product_outputs(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, page_size=None, page_token=None) -> web.Response:
    """get_provisioned_product_outputs

    This API takes either a &lt;code&gt;ProvisonedProductId&lt;/code&gt; or a &lt;code&gt;ProvisionedProductName&lt;/code&gt;, along with a list of one or more output keys, and responds with the key/value pairs of those outputs.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param page_size: Pagination limit
    :type page_size: str
    :param page_token: Pagination token
    :type page_token: str

    """
    body = GetProvisionedProductOutputsInput.from_dict(body)
    return web.Response(status=200)


async def import_as_provisioned_product(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """import_as_provisioned_product

    &lt;p&gt; Requests the import of a resource as an Service Catalog provisioned product that is associated to an Service Catalog product and provisioning artifact. Once imported, all supported governance actions are supported on the provisioned product. &lt;/p&gt; &lt;p&gt; Resource import only supports CloudFormation stack ARNs. CloudFormation StackSets, and non-root nested stacks are not supported. &lt;/p&gt; &lt;p&gt; The CloudFormation stack must have one of the following statuses to be imported: &lt;code&gt;CREATE_COMPLETE&lt;/code&gt;, &lt;code&gt;UPDATE_COMPLETE&lt;/code&gt;, &lt;code&gt;UPDATE_ROLLBACK_COMPLETE&lt;/code&gt;, &lt;code&gt;IMPORT_COMPLETE&lt;/code&gt;, and &lt;code&gt;IMPORT_ROLLBACK_COMPLETE&lt;/code&gt;. &lt;/p&gt; &lt;p&gt; Import of the resource requires that the CloudFormation stack template matches the associated Service Catalog product provisioning artifact. &lt;/p&gt; &lt;note&gt; &lt;p&gt; When you import an existing CloudFormation stack into a portfolio, constraints that are associated with the product aren&#39;t applied during the import process. The constraints are applied after you call &lt;code&gt;UpdateProvisionedProduct&lt;/code&gt; for the provisioned product. &lt;/p&gt; &lt;/note&gt; &lt;p&gt; The user or role that performs this operation must have the &lt;code&gt;cloudformation:GetTemplate&lt;/code&gt; and &lt;code&gt;cloudformation:DescribeStacks&lt;/code&gt; IAM policy permissions. &lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = ImportAsProvisionedProductInput.from_dict(body)
    return web.Response(status=200)


async def list_accepted_portfolio_shares(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, page_size=None, page_token=None) -> web.Response:
    """list_accepted_portfolio_shares

    Lists all imported portfolios for which account-to-account shares were accepted by this account. By specifying the &lt;code&gt;PortfolioShareType&lt;/code&gt;, you can list portfolios for which organizational shares were accepted by this account.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param page_size: Pagination limit
    :type page_size: str
    :param page_token: Pagination token
    :type page_token: str

    """
    body = ListAcceptedPortfolioSharesInput.from_dict(body)
    return web.Response(status=200)


async def list_budgets_for_resource(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, page_size=None, page_token=None) -> web.Response:
    """list_budgets_for_resource

    Lists all the budgets associated to the specified resource.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param page_size: Pagination limit
    :type page_size: str
    :param page_token: Pagination token
    :type page_token: str

    """
    body = ListBudgetsForResourceInput.from_dict(body)
    return web.Response(status=200)


async def list_constraints_for_portfolio(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, page_size=None, page_token=None) -> web.Response:
    """list_constraints_for_portfolio

    Lists the constraints for the specified portfolio and product.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param page_size: Pagination limit
    :type page_size: str
    :param page_token: Pagination token
    :type page_token: str

    """
    body = ListConstraintsForPortfolioInput.from_dict(body)
    return web.Response(status=200)


async def list_launch_paths(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, page_size=None, page_token=None) -> web.Response:
    """list_launch_paths

    &lt;p&gt; Lists the paths to the specified product. A path describes how the user gets access to a specified product and is necessary when provisioning a product. A path also determines the constraints that are put on a product. A path is dependent on a specific product, porfolio, and principal. &lt;/p&gt; &lt;note&gt; &lt;p&gt; When provisioning a product that&#39;s been added to a portfolio, you must grant your user, group, or role access to the portfolio. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/servicecatalog/latest/adminguide/catalogs_portfolios_users.html\&quot;&gt;Granting users access&lt;/a&gt; in the &lt;i&gt;Service Catalog User Guide&lt;/i&gt;. &lt;/p&gt; &lt;/note&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param page_size: Pagination limit
    :type page_size: str
    :param page_token: Pagination token
    :type page_token: str

    """
    body = ListLaunchPathsInput.from_dict(body)
    return web.Response(status=200)


async def list_organization_portfolio_access(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, page_size=None, page_token=None) -> web.Response:
    """list_organization_portfolio_access

    &lt;p&gt;Lists the organization nodes that have access to the specified portfolio. This API can only be called by the management account in the organization or by a delegated admin.&lt;/p&gt; &lt;p&gt;If a delegated admin is de-registered, they can no longer perform this operation.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param page_size: Pagination limit
    :type page_size: str
    :param page_token: Pagination token
    :type page_token: str

    """
    body = ListOrganizationPortfolioAccessInput.from_dict(body)
    return web.Response(status=200)


async def list_portfolio_access(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, page_size=None, page_token=None) -> web.Response:
    """list_portfolio_access

    &lt;p&gt;Lists the account IDs that have access to the specified portfolio.&lt;/p&gt; &lt;p&gt;A delegated admin can list the accounts that have access to the shared portfolio. Note that if a delegated admin is de-registered, they can no longer perform this operation.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param page_size: Pagination limit
    :type page_size: str
    :param page_token: Pagination token
    :type page_token: str

    """
    body = ListPortfolioAccessInput.from_dict(body)
    return web.Response(status=200)


async def list_portfolios(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, page_size=None, page_token=None) -> web.Response:
    """list_portfolios

    Lists all portfolios in the catalog.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param page_size: Pagination limit
    :type page_size: str
    :param page_token: Pagination token
    :type page_token: str

    """
    body = ListPortfoliosInput.from_dict(body)
    return web.Response(status=200)


async def list_portfolios_for_product(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, page_size=None, page_token=None) -> web.Response:
    """list_portfolios_for_product

    Lists all portfolios that the specified product is associated with.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param page_size: Pagination limit
    :type page_size: str
    :param page_token: Pagination token
    :type page_token: str

    """
    body = ListPortfoliosForProductInput.from_dict(body)
    return web.Response(status=200)


async def list_principals_for_portfolio(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, page_size=None, page_token=None) -> web.Response:
    """list_principals_for_portfolio

    Lists all &lt;code&gt;PrincipalARN&lt;/code&gt;s and corresponding &lt;code&gt;PrincipalType&lt;/code&gt;s associated with the specified portfolio.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param page_size: Pagination limit
    :type page_size: str
    :param page_token: Pagination token
    :type page_token: str

    """
    body = ListPrincipalsForPortfolioInput.from_dict(body)
    return web.Response(status=200)


async def list_provisioned_product_plans(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_provisioned_product_plans

    Lists the plans for the specified provisioned product or all plans to which the user has access.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = ListProvisionedProductPlansInput.from_dict(body)
    return web.Response(status=200)


async def list_provisioning_artifacts(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_provisioning_artifacts

    Lists all provisioning artifacts (also known as versions) for the specified product.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = ListProvisioningArtifactsInput.from_dict(body)
    return web.Response(status=200)


async def list_provisioning_artifacts_for_service_action(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, page_size=None, page_token=None) -> web.Response:
    """list_provisioning_artifacts_for_service_action

    Lists all provisioning artifacts (also known as versions) for the specified self-service action.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param page_size: Pagination limit
    :type page_size: str
    :param page_token: Pagination token
    :type page_token: str

    """
    body = ListProvisioningArtifactsForServiceActionInput.from_dict(body)
    return web.Response(status=200)


async def list_record_history(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_record_history

    Lists the specified requests or all performed requests.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = ListRecordHistoryInput.from_dict(body)
    return web.Response(status=200)


async def list_resources_for_tag_option(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, page_size=None, page_token=None) -> web.Response:
    """list_resources_for_tag_option

    Lists the resources associated with the specified TagOption.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param page_size: Pagination limit
    :type page_size: str
    :param page_token: Pagination token
    :type page_token: str

    """
    body = ListResourcesForTagOptionInput.from_dict(body)
    return web.Response(status=200)


async def list_service_actions(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, page_size=None, page_token=None) -> web.Response:
    """list_service_actions

    Lists all self-service actions.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param page_size: Pagination limit
    :type page_size: str
    :param page_token: Pagination token
    :type page_token: str

    """
    body = ListServiceActionsInput.from_dict(body)
    return web.Response(status=200)


async def list_service_actions_for_provisioning_artifact(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, page_size=None, page_token=None) -> web.Response:
    """list_service_actions_for_provisioning_artifact

    Returns a paginated list of self-service actions associated with the specified Product ID and Provisioning Artifact ID.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param page_size: Pagination limit
    :type page_size: str
    :param page_token: Pagination token
    :type page_token: str

    """
    body = ListServiceActionsForProvisioningArtifactInput.from_dict(body)
    return web.Response(status=200)


async def list_stack_instances_for_provisioned_product(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_stack_instances_for_provisioned_product

    Returns summary information about stack instances that are associated with the specified &lt;code&gt;CFN_STACKSET&lt;/code&gt; type provisioned product. You can filter for stack instances that are associated with a specific Amazon Web Services account name or Region. 

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = ListStackInstancesForProvisionedProductInput.from_dict(body)
    return web.Response(status=200)


async def list_tag_options(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, page_size=None, page_token=None) -> web.Response:
    """list_tag_options

    Lists the specified TagOptions or all TagOptions.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param page_size: Pagination limit
    :type page_size: str
    :param page_token: Pagination token
    :type page_token: str

    """
    body = ListTagOptionsInput.from_dict(body)
    return web.Response(status=200)


async def notify_provision_product_engine_workflow_result(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """notify_provision_product_engine_workflow_result

     Notifies the result of the provisioning engine execution. 

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = NotifyProvisionProductEngineWorkflowResultInput.from_dict(body)
    return web.Response(status=200)


async def notify_terminate_provisioned_product_engine_workflow_result(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """notify_terminate_provisioned_product_engine_workflow_result

     Notifies the result of the terminate engine execution. 

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = NotifyTerminateProvisionedProductEngineWorkflowResultInput.from_dict(body)
    return web.Response(status=200)


async def notify_update_provisioned_product_engine_workflow_result(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """notify_update_provisioned_product_engine_workflow_result

     Notifies the result of the update engine execution. 

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = NotifyUpdateProvisionedProductEngineWorkflowResultInput.from_dict(body)
    return web.Response(status=200)


async def provision_product(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """provision_product

    &lt;p&gt; Provisions the specified product. &lt;/p&gt; &lt;p&gt; A provisioned product is a resourced instance of a product. For example, provisioning a product that&#39;s based on an CloudFormation template launches an CloudFormation stack and its underlying resources. You can check the status of this request using &lt;a&gt;DescribeRecord&lt;/a&gt;. &lt;/p&gt; &lt;p&gt; If the request contains a tag key with an empty list of values, there&#39;s a tag conflict for that key. Don&#39;t include conflicted keys as tags, or this will cause the error \&quot;Parameter validation failed: Missing required parameter in Tags[&lt;i&gt;N&lt;/i&gt;]:&lt;i&gt;Value&lt;/i&gt;\&quot;. &lt;/p&gt; &lt;note&gt; &lt;p&gt; When provisioning a product that&#39;s been added to a portfolio, you must grant your user, group, or role access to the portfolio. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/servicecatalog/latest/adminguide/catalogs_portfolios_users.html\&quot;&gt;Granting users access&lt;/a&gt; in the &lt;i&gt;Service Catalog User Guide&lt;/i&gt;. &lt;/p&gt; &lt;/note&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = ProvisionProductInput.from_dict(body)
    return web.Response(status=200)


async def reject_portfolio_share(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """reject_portfolio_share

    Rejects an offer to share the specified portfolio.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = RejectPortfolioShareInput.from_dict(body)
    return web.Response(status=200)


async def scan_provisioned_products(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """scan_provisioned_products

    &lt;p&gt;Lists the provisioned products that are available (not terminated).&lt;/p&gt; &lt;p&gt;To use additional filtering, see &lt;a&gt;SearchProvisionedProducts&lt;/a&gt;.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = ScanProvisionedProductsInput.from_dict(body)
    return web.Response(status=200)


async def search_products(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, page_size=None, page_token=None) -> web.Response:
    """search_products

    Gets information about the products to which the caller has access.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param page_size: Pagination limit
    :type page_size: str
    :param page_token: Pagination token
    :type page_token: str

    """
    body = SearchProductsInput.from_dict(body)
    return web.Response(status=200)


async def search_products_as_admin(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, page_size=None, page_token=None) -> web.Response:
    """search_products_as_admin

    Gets information about the products for the specified portfolio or all products.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param page_size: Pagination limit
    :type page_size: str
    :param page_token: Pagination token
    :type page_token: str

    """
    body = SearchProductsAsAdminInput.from_dict(body)
    return web.Response(status=200)


async def search_provisioned_products(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, page_size=None, page_token=None) -> web.Response:
    """search_provisioned_products

    Gets information about the provisioned products that meet the specified criteria.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param page_size: Pagination limit
    :type page_size: str
    :param page_token: Pagination token
    :type page_token: str

    """
    body = SearchProvisionedProductsInput.from_dict(body)
    return web.Response(status=200)


async def terminate_provisioned_product(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """terminate_provisioned_product

    &lt;p&gt;Terminates the specified provisioned product.&lt;/p&gt; &lt;p&gt;This operation does not delete any records associated with the provisioned product.&lt;/p&gt; &lt;p&gt;You can check the status of this request using &lt;a&gt;DescribeRecord&lt;/a&gt;.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = TerminateProvisionedProductInput.from_dict(body)
    return web.Response(status=200)


async def update_constraint(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_constraint

    Updates the specified constraint.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateConstraintInput.from_dict(body)
    return web.Response(status=200)


async def update_portfolio(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_portfolio

    &lt;p&gt;Updates the specified portfolio.&lt;/p&gt; &lt;p&gt;You cannot update a product that was shared with you.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdatePortfolioInput.from_dict(body)
    return web.Response(status=200)


async def update_portfolio_share(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_portfolio_share

    &lt;p&gt;Updates the specified portfolio share. You can use this API to enable or disable &lt;code&gt;TagOptions&lt;/code&gt; sharing or Principal sharing for an existing portfolio share. &lt;/p&gt; &lt;p&gt;The portfolio share cannot be updated if the &lt;code&gt;CreatePortfolioShare&lt;/code&gt; operation is &lt;code&gt;IN_PROGRESS&lt;/code&gt;, as the share is not available to recipient entities. In this case, you must wait for the portfolio share to be COMPLETED.&lt;/p&gt; &lt;p&gt;You must provide the &lt;code&gt;accountId&lt;/code&gt; or organization node in the input, but not both.&lt;/p&gt; &lt;p&gt;If the portfolio is shared to both an external account and an organization node, and both shares need to be updated, you must invoke &lt;code&gt;UpdatePortfolioShare&lt;/code&gt; separately for each share type. &lt;/p&gt; &lt;p&gt;This API cannot be used for removing the portfolio share. You must use &lt;code&gt;DeletePortfolioShare&lt;/code&gt; API for that action. &lt;/p&gt; &lt;note&gt; &lt;p&gt;When you associate a principal with portfolio, a potential privilege escalation path may occur when that portfolio is then shared with other accounts. For a user in a recipient account who is &lt;i&gt;not&lt;/i&gt; an Service Catalog Admin, but still has the ability to create Principals (Users/Groups/Roles), that user could create a role that matches a principal name association for the portfolio. Although this user may not know which principal names are associated through Service Catalog, they may be able to guess the user. If this potential escalation path is a concern, then Service Catalog recommends using &lt;code&gt;PrincipalType&lt;/code&gt; as &lt;code&gt;IAM&lt;/code&gt;. With this configuration, the &lt;code&gt;PrincipalARN&lt;/code&gt; must already exist in the recipient account before it can be associated. &lt;/p&gt; &lt;/note&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdatePortfolioShareInput.from_dict(body)
    return web.Response(status=200)


async def update_product(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_product

    Updates the specified product.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateProductInput.from_dict(body)
    return web.Response(status=200)


async def update_provisioned_product(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_provisioned_product

    &lt;p&gt;Requests updates to the configuration of the specified provisioned product.&lt;/p&gt; &lt;p&gt;If there are tags associated with the object, they cannot be updated or added. Depending on the specific updates requested, this operation can update with no interruption, with some interruption, or replace the provisioned product entirely.&lt;/p&gt; &lt;p&gt;You can check the status of this request using &lt;a&gt;DescribeRecord&lt;/a&gt;.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateProvisionedProductInput.from_dict(body)
    return web.Response(status=200)


async def update_provisioned_product_properties(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_provisioned_product_properties

    Requests updates to the properties of the specified provisioned product.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateProvisionedProductPropertiesInput.from_dict(body)
    return web.Response(status=200)


async def update_provisioning_artifact(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_provisioning_artifact

    &lt;p&gt;Updates the specified provisioning artifact (also known as a version) for the specified product.&lt;/p&gt; &lt;p&gt;You cannot update a provisioning artifact for a product that was shared with you.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateProvisioningArtifactInput.from_dict(body)
    return web.Response(status=200)


async def update_service_action(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_service_action

    Updates a self-service action.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateServiceActionInput.from_dict(body)
    return web.Response(status=200)


async def update_tag_option(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_tag_option

    Updates the specified TagOption.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateTagOptionInput.from_dict(body)
    return web.Response(status=200)
