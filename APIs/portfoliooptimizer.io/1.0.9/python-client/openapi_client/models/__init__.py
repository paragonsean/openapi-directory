# coding: utf-8

# flake8: noqa
"""
    Portfolio Optimizer

    Portfolio Optimizer is a [Web API](https://en.wikipedia.org/wiki/Web_API) to analyze and optimize investment portfolios (collection of financial assets such as stocks, bonds, ETFs, crypto-currencies) using modern portfolio theory algorithms (mean-variance, VaR, etc.).  # API General Information    Portfolio Optimizer is based on [REST](https://en.wikipedia.org/wiki/Representational_state_transfer) for easy integration, uses [JSON](https://en.wikipedia.org/wiki/JSON) for the exchange of data and uses a standard [HTTP verb](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol#Request_methods) (`POST`) to represent the action(s).  Portfolio Optimizer is also as secured as a Web API could be:  * [256-bit HTTPS Encryption](https://en.wikipedia.org/wiki/HTTPS) * No usage of cookies * No usage of personal data    ## API Headers  The following HTTP header(s) are required when calling Portfolio Optimizer endpoints: * `Content-type: application/json`     This header specifies that the data provided in input to the endpoint is in JSON format  The following HTTP header(s) are optional when calling Portfolio Optimizer endpoints: * `Content-Encoding: gzip`     This header indicates that the data provided in input to the endpoint is compressed with gzip. * `X-API-Key: <private API key>`     This header enables [authenticated users](#auth) to provide their private [API key](#overview--api-key) in order to [benefit from higher API limits](#overview--api-limits)  ## API Key Portfolio Optimizer is free to use, but not free to run.  In order to obtain an API key and benefit from [higher API limits](#overview--api-limits), a *small* participation to Portfolio Optimizer running costs is required.  This participation takes the form of coffee(s), with one coffee = one month of usage.  <p><a href=\"https://www.buymeacoffee.com/portfolioopt\"><img alt='Buy a Coffee at buymeacoffee.com' src=\"https://img.buymeacoffee.com/button-api/?text=Buymeacoffee.com&emoji=&slug=portfolioopt&button_colour=000000&font_colour=ffffff&font_family=Cookie&outline_colour=ffffff&coffee_colour=FFDD00\"></a></p>   > **Notes:**  > * Please make sure not to expose your API key publicly!  ## API Limits   Portfolio Optimizer comes with *fairly reasonable* API limits.  For anonymous users:   * The API requests are restricted to a subset of all the available endpoints and/or endpoints features   * The API requests are limited to 1 request per second for all the anonymous users combined, with concurrent requests rejected  * The API requests are limited to 1 second of execution time * The API requests are limited to 20 assets, 250 portfolios, 500 series data points and 5 factors  For authenticated users with an [API key](#overview--api-key):   * The API requests have access to all the available endpoints and endpoints features * The API requests are limited to 10000 requests per 24 hour per API key, with concurrent requests queued * The API requests are limited to 2.5 seconds of execution time * The API requests are limited to 100 assets, 1250 portfolios, 2500 series data points and 25 factors  > **Notes:**  > * It is possible to further relax the API limits, or to disable the API limits alltogether; please [contact the support](https://portfoliooptimizer.io/contact/) for more details. > * Information on the API rate limits are provided in response messages HTTP headers `x-ratelimit-*`:   >   * `x-ratelimit-limit-second`, the limit on the number of API requests per second >   * `x-ratelimit-remaining-second`, the number of remaining API requests in the current second     >   * `x-ratelimit-limit-minute`, the limit on the number of API requests per minute >   * ...  ## API Regions Portfolio Optimizer servers are located in Western Europe.  > **Notes:**  > * It is possible to deploy Portfolio Optimizer in other geographical regions, for example to improve the API latency; please [contact the support](https://portfoliooptimizer.io/contact/) for more details.   ## API Response Codes         Standard [HTTP response codes](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes) are used by Portfolio Optimizer to provide details on the status of API requests.  | HTTP Code | Description | Notes | | --------- | ----------- | ----- | | 200 | Request successfully processed | - | | 400 | Request failed to be processed because of incorrect content | The response message body contains information on the incorrect content | | 401 | Request failed to be processed because of invalid API key | - | | 404 | Request failed to be processed because of non existing endpoint | The requested endpoint might exist, but needs to be accessed with another HTTP method (e.g., `POST` instead of `GET`) | | 429 | Request failed to be processed because of API limits violated | The response message HTTP headers `x-ratelimit-*` contain information on the [API limits](#overview--api-limits) | | 500 | Request failed to be processed because of an internal error | Something went wrong on Portfolio Optimizer side, do not hesitate to [report the issue](#overview--support) | | 502 | Request failed to be processed because of a temporary connectivity error | Something went wrong on Portfolio Optimizer side, please check the [API status](#overview--api-status) and do not hesitate to [report the issue](#overview--support) |  ## API Status    Portfolio Optimizer is monitored 24/7 by [UptimeRobot](https://stats.uptimerobot.com/wgW71SL1AW).  # Support  For any issue or question about Portfolio Optimizer, please do not hesitate to [contact the support](https://portfoliooptimizer.io/contact/). 

    The version of the OpenAPI document: 1.0.9
    Contact: contact@portfoliooptimizer.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


# import models into model package
from openapi_client.models.assets_analysis_absorption_ratio_post200_response import AssetsAnalysisAbsorptionRatioPost200Response
from openapi_client.models.assets_analysis_absorption_ratio_post_request import AssetsAnalysisAbsorptionRatioPostRequest
from openapi_client.models.assets_analysis_absorption_ratio_post_request_assets_covariance_matrix_eigenvectors import AssetsAnalysisAbsorptionRatioPostRequestAssetsCovarianceMatrixEigenvectors
from openapi_client.models.assets_analysis_turbulence_index_post200_response import AssetsAnalysisTurbulenceIndexPost200Response
from openapi_client.models.assets_analysis_turbulence_index_post_request import AssetsAnalysisTurbulenceIndexPostRequest
from openapi_client.models.assets_correlation_matrix_bounds_post200_response import AssetsCorrelationMatrixBoundsPost200Response
from openapi_client.models.assets_correlation_matrix_bounds_post_request import AssetsCorrelationMatrixBoundsPostRequest
from openapi_client.models.assets_correlation_matrix_denoised_post200_response import AssetsCorrelationMatrixDenoisedPost200Response
from openapi_client.models.assets_correlation_matrix_denoised_post_request import AssetsCorrelationMatrixDenoisedPostRequest
from openapi_client.models.assets_correlation_matrix_distance_post200_response import AssetsCorrelationMatrixDistancePost200Response
from openapi_client.models.assets_correlation_matrix_distance_post_request import AssetsCorrelationMatrixDistancePostRequest
from openapi_client.models.assets_correlation_matrix_effective_rank_post200_response import AssetsCorrelationMatrixEffectiveRankPost200Response
from openapi_client.models.assets_correlation_matrix_effective_rank_post_request import AssetsCorrelationMatrixEffectiveRankPostRequest
from openapi_client.models.assets_correlation_matrix_informativeness_post200_response import AssetsCorrelationMatrixInformativenessPost200Response
from openapi_client.models.assets_correlation_matrix_informativeness_post_request import AssetsCorrelationMatrixInformativenessPostRequest
from openapi_client.models.assets_correlation_matrix_nearest_post_request import AssetsCorrelationMatrixNearestPostRequest
from openapi_client.models.assets_correlation_matrix_post200_response import AssetsCorrelationMatrixPost200Response
from openapi_client.models.assets_correlation_matrix_post_request import AssetsCorrelationMatrixPostRequest
from openapi_client.models.assets_correlation_matrix_post_request_one_of import AssetsCorrelationMatrixPostRequestOneOf
from openapi_client.models.assets_correlation_matrix_post_request_one_of1 import AssetsCorrelationMatrixPostRequestOneOf1
from openapi_client.models.assets_correlation_matrix_post_request_one_of_assets_inner import AssetsCorrelationMatrixPostRequestOneOfAssetsInner
from openapi_client.models.assets_correlation_matrix_random_post_request import AssetsCorrelationMatrixRandomPostRequest
from openapi_client.models.assets_correlation_matrix_shrinkage_post_request import AssetsCorrelationMatrixShrinkagePostRequest
from openapi_client.models.assets_correlation_matrix_shrinkage_post_request_one_of import AssetsCorrelationMatrixShrinkagePostRequestOneOf
from openapi_client.models.assets_correlation_matrix_shrinkage_post_request_one_of1 import AssetsCorrelationMatrixShrinkagePostRequestOneOf1
from openapi_client.models.assets_correlation_matrix_theory_implied_post_request import AssetsCorrelationMatrixTheoryImpliedPostRequest
from openapi_client.models.assets_correlation_matrix_theory_implied_post_request_assets_inner import AssetsCorrelationMatrixTheoryImpliedPostRequestAssetsInner
from openapi_client.models.assets_correlation_matrix_theory_implied_post_request_assets_inner_asset_hierarchical_classification_inner import AssetsCorrelationMatrixTheoryImpliedPostRequestAssetsInnerAssetHierarchicalClassificationInner
from openapi_client.models.assets_correlation_matrix_validation_post200_response import AssetsCorrelationMatrixValidationPost200Response
from openapi_client.models.assets_correlation_matrix_validation_post_request import AssetsCorrelationMatrixValidationPostRequest
from openapi_client.models.assets_covariance_matrix_effective_rank_post200_response import AssetsCovarianceMatrixEffectiveRankPost200Response
from openapi_client.models.assets_covariance_matrix_effective_rank_post_request import AssetsCovarianceMatrixEffectiveRankPostRequest
from openapi_client.models.assets_covariance_matrix_exponentially_weighted_post200_response import AssetsCovarianceMatrixExponentiallyWeightedPost200Response
from openapi_client.models.assets_covariance_matrix_exponentially_weighted_post_request import AssetsCovarianceMatrixExponentiallyWeightedPostRequest
from openapi_client.models.assets_covariance_matrix_post200_response import AssetsCovarianceMatrixPost200Response
from openapi_client.models.assets_covariance_matrix_post_request import AssetsCovarianceMatrixPostRequest
from openapi_client.models.assets_covariance_matrix_post_request_one_of import AssetsCovarianceMatrixPostRequestOneOf
from openapi_client.models.assets_covariance_matrix_post_request_one_of1 import AssetsCovarianceMatrixPostRequestOneOf1
from openapi_client.models.assets_covariance_matrix_validation_post200_response import AssetsCovarianceMatrixValidationPost200Response
from openapi_client.models.assets_kurtosis_post200_response import AssetsKurtosisPost200Response
from openapi_client.models.assets_kurtosis_post200_response_assets_inner import AssetsKurtosisPost200ResponseAssetsInner
from openapi_client.models.assets_kurtosis_post_request import AssetsKurtosisPostRequest
from openapi_client.models.assets_kurtosis_post_request_assets_inner import AssetsKurtosisPostRequestAssetsInner
from openapi_client.models.assets_prices_adjusted_post200_response import AssetsPricesAdjustedPost200Response
from openapi_client.models.assets_prices_adjusted_post200_response_assets_inner import AssetsPricesAdjustedPost200ResponseAssetsInner
from openapi_client.models.assets_prices_adjusted_post200_response_assets_inner_asset_adjusted_prices_inner import AssetsPricesAdjustedPost200ResponseAssetsInnerAssetAdjustedPricesInner
from openapi_client.models.assets_prices_adjusted_post_request import AssetsPricesAdjustedPostRequest
from openapi_client.models.assets_prices_adjusted_post_request_assets_inner import AssetsPricesAdjustedPostRequestAssetsInner
from openapi_client.models.assets_prices_adjusted_post_request_assets_inner_asset_dividends_inner import AssetsPricesAdjustedPostRequestAssetsInnerAssetDividendsInner
from openapi_client.models.assets_prices_adjusted_post_request_assets_inner_asset_prices_inner import AssetsPricesAdjustedPostRequestAssetsInnerAssetPricesInner
from openapi_client.models.assets_prices_adjusted_post_request_assets_inner_asset_splits_inner import AssetsPricesAdjustedPostRequestAssetsInnerAssetSplitsInner
from openapi_client.models.assets_returns_average_post200_response import AssetsReturnsAveragePost200Response
from openapi_client.models.assets_returns_average_post200_response_assets_inner import AssetsReturnsAveragePost200ResponseAssetsInner
from openapi_client.models.assets_returns_average_post_request import AssetsReturnsAveragePostRequest
from openapi_client.models.assets_returns_average_post_request_assets_inner import AssetsReturnsAveragePostRequestAssetsInner
from openapi_client.models.assets_returns_logarithmic_post200_response import AssetsReturnsLogarithmicPost200Response
from openapi_client.models.assets_returns_logarithmic_post200_response_assets_inner import AssetsReturnsLogarithmicPost200ResponseAssetsInner
from openapi_client.models.assets_returns_post200_response import AssetsReturnsPost200Response
from openapi_client.models.assets_returns_post200_response_assets_inner import AssetsReturnsPost200ResponseAssetsInner
from openapi_client.models.assets_returns_post_request import AssetsReturnsPostRequest
from openapi_client.models.assets_returns_post_request_assets_inner import AssetsReturnsPostRequestAssetsInner
from openapi_client.models.assets_returns_simulation_bootstrap_post200_response import AssetsReturnsSimulationBootstrapPost200Response
from openapi_client.models.assets_returns_simulation_bootstrap_post200_response_simulations_inner import AssetsReturnsSimulationBootstrapPost200ResponseSimulationsInner
from openapi_client.models.assets_returns_simulation_bootstrap_post200_response_simulations_inner_assets_inner import AssetsReturnsSimulationBootstrapPost200ResponseSimulationsInnerAssetsInner
from openapi_client.models.assets_returns_simulation_bootstrap_post_request import AssetsReturnsSimulationBootstrapPostRequest
from openapi_client.models.assets_returns_simulation_bootstrap_post_request_assets_inner import AssetsReturnsSimulationBootstrapPostRequestAssetsInner
from openapi_client.models.assets_returns_simulation_monte_carlo_cornish_fisher_corrected_post_request import AssetsReturnsSimulationMonteCarloCornishFisherCorrectedPostRequest
from openapi_client.models.assets_returns_simulation_monte_carlo_cornish_fisher_post200_response import AssetsReturnsSimulationMonteCarloCornishFisherPost200Response
from openapi_client.models.assets_returns_simulation_monte_carlo_cornish_fisher_post200_response_simulations_inner import AssetsReturnsSimulationMonteCarloCornishFisherPost200ResponseSimulationsInner
from openapi_client.models.assets_returns_simulation_monte_carlo_cornish_fisher_post_request import AssetsReturnsSimulationMonteCarloCornishFisherPostRequest
from openapi_client.models.assets_returns_simulation_monte_carlo_gaussian_post_request import AssetsReturnsSimulationMonteCarloGaussianPostRequest
from openapi_client.models.assets_returns_turbulence_partitioned_post200_response import AssetsReturnsTurbulencePartitionedPost200Response
from openapi_client.models.assets_returns_turbulence_partitioned_post200_response_assets_inner import AssetsReturnsTurbulencePartitionedPost200ResponseAssetsInner
from openapi_client.models.assets_returns_turbulence_partitioned_post200_response_assets_inner_asset_turbulence_partitioned_returns_inner import AssetsReturnsTurbulencePartitionedPost200ResponseAssetsInnerAssetTurbulencePartitionedReturnsInner
from openapi_client.models.assets_returns_turbulence_partitioned_post_request import AssetsReturnsTurbulencePartitionedPostRequest
from openapi_client.models.assets_skewness_post200_response import AssetsSkewnessPost200Response
from openapi_client.models.assets_skewness_post200_response_assets_inner import AssetsSkewnessPost200ResponseAssetsInner
from openapi_client.models.assets_skewness_post_request import AssetsSkewnessPostRequest
from openapi_client.models.assets_skewness_post_request_assets_inner import AssetsSkewnessPostRequestAssetsInner
from openapi_client.models.assets_variance_post200_response import AssetsVariancePost200Response
from openapi_client.models.assets_variance_post200_response_assets_inner import AssetsVariancePost200ResponseAssetsInner
from openapi_client.models.assets_variance_post_request import AssetsVariancePostRequest
from openapi_client.models.assets_variance_post_request_one_of import AssetsVariancePostRequestOneOf
from openapi_client.models.assets_variance_post_request_one_of1 import AssetsVariancePostRequestOneOf1
from openapi_client.models.assets_variance_post_request_one_of1_assets_inner import AssetsVariancePostRequestOneOf1AssetsInner
from openapi_client.models.assets_variance_post_request_one_of_assets_inner import AssetsVariancePostRequestOneOfAssetsInner
from openapi_client.models.assets_volatility_post200_response import AssetsVolatilityPost200Response
from openapi_client.models.assets_volatility_post200_response_assets_inner import AssetsVolatilityPost200ResponseAssetsInner
from openapi_client.models.assets_volatility_post_request import AssetsVolatilityPostRequest
from openapi_client.models.assets_volatility_post_request_one_of import AssetsVolatilityPostRequestOneOf
from openapi_client.models.assets_volatility_post_request_one_of_assets_inner import AssetsVolatilityPostRequestOneOfAssetsInner
from openapi_client.models.factors_residualization_post200_response import FactorsResidualizationPost200Response
from openapi_client.models.factors_residualization_post_request import FactorsResidualizationPostRequest
from openapi_client.models.factors_residualization_post_request_factors_inner import FactorsResidualizationPostRequestFactorsInner
from openapi_client.models.portfolio_analysis_alpha_post200_response import PortfolioAnalysisAlphaPost200Response
from openapi_client.models.portfolio_analysis_alpha_post200_response_portfolios_inner import PortfolioAnalysisAlphaPost200ResponsePortfoliosInner
from openapi_client.models.portfolio_analysis_alpha_post_request import PortfolioAnalysisAlphaPostRequest
from openapi_client.models.portfolio_analysis_alpha_post_request_one_of import PortfolioAnalysisAlphaPostRequestOneOf
from openapi_client.models.portfolio_analysis_alpha_post_request_one_of1 import PortfolioAnalysisAlphaPostRequestOneOf1
from openapi_client.models.portfolio_analysis_alpha_post_request_one_of_portfolios_inner import PortfolioAnalysisAlphaPostRequestOneOfPortfoliosInner
from openapi_client.models.portfolio_analysis_beta_post200_response import PortfolioAnalysisBetaPost200Response
from openapi_client.models.portfolio_analysis_beta_post200_response_portfolios_inner import PortfolioAnalysisBetaPost200ResponsePortfoliosInner
from openapi_client.models.portfolio_analysis_contributions_return_post200_response import PortfolioAnalysisContributionsReturnPost200Response
from openapi_client.models.portfolio_analysis_contributions_return_post200_response_portfolios_inner import PortfolioAnalysisContributionsReturnPost200ResponsePortfoliosInner
from openapi_client.models.portfolio_analysis_contributions_return_post_request import PortfolioAnalysisContributionsReturnPostRequest
from openapi_client.models.portfolio_analysis_contributions_return_post_request_portfolios_inner import PortfolioAnalysisContributionsReturnPostRequestPortfoliosInner
from openapi_client.models.portfolio_analysis_contributions_risk_post200_response import PortfolioAnalysisContributionsRiskPost200Response
from openapi_client.models.portfolio_analysis_contributions_risk_post200_response_portfolios_inner import PortfolioAnalysisContributionsRiskPost200ResponsePortfoliosInner
from openapi_client.models.portfolio_analysis_contributions_risk_post_request import PortfolioAnalysisContributionsRiskPostRequest
from openapi_client.models.portfolio_analysis_correlation_spectrum_post200_response import PortfolioAnalysisCorrelationSpectrumPost200Response
from openapi_client.models.portfolio_analysis_correlation_spectrum_post200_response_portfolios_inner import PortfolioAnalysisCorrelationSpectrumPost200ResponsePortfoliosInner
from openapi_client.models.portfolio_analysis_correlation_spectrum_post_request import PortfolioAnalysisCorrelationSpectrumPostRequest
from openapi_client.models.portfolio_analysis_correlation_spectrum_post_request_one_of import PortfolioAnalysisCorrelationSpectrumPostRequestOneOf
from openapi_client.models.portfolio_analysis_correlation_spectrum_post_request_one_of1 import PortfolioAnalysisCorrelationSpectrumPostRequestOneOf1
from openapi_client.models.portfolio_analysis_correlation_spectrum_post_request_one_of1_assets_inner import PortfolioAnalysisCorrelationSpectrumPostRequestOneOf1AssetsInner
from openapi_client.models.portfolio_analysis_correlation_spectrum_post_request_one_of1_portfolios_inner import PortfolioAnalysisCorrelationSpectrumPostRequestOneOf1PortfoliosInner
from openapi_client.models.portfolio_analysis_diversification_ratio_post200_response import PortfolioAnalysisDiversificationRatioPost200Response
from openapi_client.models.portfolio_analysis_diversification_ratio_post200_response_portfolios_inner import PortfolioAnalysisDiversificationRatioPost200ResponsePortfoliosInner
from openapi_client.models.portfolio_analysis_drawdowns_post200_response import PortfolioAnalysisDrawdownsPost200Response
from openapi_client.models.portfolio_analysis_drawdowns_post200_response_portfolios_inner import PortfolioAnalysisDrawdownsPost200ResponsePortfoliosInner
from openapi_client.models.portfolio_analysis_drawdowns_post200_response_portfolios_inner_portfolio_worst_drawdowns_inner import PortfolioAnalysisDrawdownsPost200ResponsePortfoliosInnerPortfolioWorstDrawdownsInner
from openapi_client.models.portfolio_analysis_drawdowns_post_request import PortfolioAnalysisDrawdownsPostRequest
from openapi_client.models.portfolio_analysis_drawdowns_post_request_portfolios_inner import PortfolioAnalysisDrawdownsPostRequestPortfoliosInner
from openapi_client.models.portfolio_analysis_effective_number_of_bets_post200_response import PortfolioAnalysisEffectiveNumberOfBetsPost200Response
from openapi_client.models.portfolio_analysis_effective_number_of_bets_post200_response_portfolios_inner import PortfolioAnalysisEffectiveNumberOfBetsPost200ResponsePortfoliosInner
from openapi_client.models.portfolio_analysis_effective_number_of_bets_post_request import PortfolioAnalysisEffectiveNumberOfBetsPostRequest
from openapi_client.models.portfolio_analysis_effective_number_of_bets_post_request_portfolios_inner import PortfolioAnalysisEffectiveNumberOfBetsPostRequestPortfoliosInner
from openapi_client.models.portfolio_analysis_factors_exposures_post200_response import PortfolioAnalysisFactorsExposuresPost200Response
from openapi_client.models.portfolio_analysis_factors_exposures_post200_response_portfolios_inner import PortfolioAnalysisFactorsExposuresPost200ResponsePortfoliosInner
from openapi_client.models.portfolio_analysis_factors_exposures_post_request import PortfolioAnalysisFactorsExposuresPostRequest
from openapi_client.models.portfolio_analysis_factors_exposures_post_request_factors_inner import PortfolioAnalysisFactorsExposuresPostRequestFactorsInner
from openapi_client.models.portfolio_analysis_factors_exposures_post_request_portfolios_inner import PortfolioAnalysisFactorsExposuresPostRequestPortfoliosInner
from openapi_client.models.portfolio_analysis_mean_variance_efficient_frontier_post200_response import PortfolioAnalysisMeanVarianceEfficientFrontierPost200Response
from openapi_client.models.portfolio_analysis_mean_variance_efficient_frontier_post200_response_portfolios_inner import PortfolioAnalysisMeanVarianceEfficientFrontierPost200ResponsePortfoliosInner
from openapi_client.models.portfolio_analysis_mean_variance_efficient_frontier_post_request import PortfolioAnalysisMeanVarianceEfficientFrontierPostRequest
from openapi_client.models.portfolio_analysis_mean_variance_efficient_frontier_post_request_constraints import PortfolioAnalysisMeanVarianceEfficientFrontierPostRequestConstraints
from openapi_client.models.portfolio_analysis_mean_variance_minimum_variance_frontier_post_request import PortfolioAnalysisMeanVarianceMinimumVarianceFrontierPostRequest
from openapi_client.models.portfolio_analysis_return_post200_response import PortfolioAnalysisReturnPost200Response
from openapi_client.models.portfolio_analysis_return_post200_response_portfolios_inner import PortfolioAnalysisReturnPost200ResponsePortfoliosInner
from openapi_client.models.portfolio_analysis_return_post_request import PortfolioAnalysisReturnPostRequest
from openapi_client.models.portfolio_analysis_return_post_request_one_of import PortfolioAnalysisReturnPostRequestOneOf
from openapi_client.models.portfolio_analysis_return_post_request_one_of1 import PortfolioAnalysisReturnPostRequestOneOf1
from openapi_client.models.portfolio_analysis_return_post_request_one_of1_portfolios_inner import PortfolioAnalysisReturnPostRequestOneOf1PortfoliosInner
from openapi_client.models.portfolio_analysis_returns_average_post200_response import PortfolioAnalysisReturnsAveragePost200Response
from openapi_client.models.portfolio_analysis_returns_average_post200_response_portfolios_inner import PortfolioAnalysisReturnsAveragePost200ResponsePortfoliosInner
from openapi_client.models.portfolio_analysis_sharpe_ratio_bias_adjusted_post200_response import PortfolioAnalysisSharpeRatioBiasAdjustedPost200Response
from openapi_client.models.portfolio_analysis_sharpe_ratio_bias_adjusted_post200_response_portfolios_inner import PortfolioAnalysisSharpeRatioBiasAdjustedPost200ResponsePortfoliosInner
from openapi_client.models.portfolio_analysis_sharpe_ratio_bias_adjusted_post_request import PortfolioAnalysisSharpeRatioBiasAdjustedPostRequest
from openapi_client.models.portfolio_analysis_sharpe_ratio_bias_adjusted_post_request_portfolios_inner import PortfolioAnalysisSharpeRatioBiasAdjustedPostRequestPortfoliosInner
from openapi_client.models.portfolio_analysis_sharpe_ratio_confidence_interval_post200_response import PortfolioAnalysisSharpeRatioConfidenceIntervalPost200Response
from openapi_client.models.portfolio_analysis_sharpe_ratio_confidence_interval_post200_response_portfolios_inner import PortfolioAnalysisSharpeRatioConfidenceIntervalPost200ResponsePortfoliosInner
from openapi_client.models.portfolio_analysis_sharpe_ratio_confidence_interval_post_request import PortfolioAnalysisSharpeRatioConfidenceIntervalPostRequest
from openapi_client.models.portfolio_analysis_sharpe_ratio_post200_response import PortfolioAnalysisSharpeRatioPost200Response
from openapi_client.models.portfolio_analysis_sharpe_ratio_post200_response_portfolios_inner import PortfolioAnalysisSharpeRatioPost200ResponsePortfoliosInner
from openapi_client.models.portfolio_analysis_sharpe_ratio_post_request import PortfolioAnalysisSharpeRatioPostRequest
from openapi_client.models.portfolio_analysis_sharpe_ratio_post_request_one_of import PortfolioAnalysisSharpeRatioPostRequestOneOf
from openapi_client.models.portfolio_analysis_sharpe_ratio_post_request_one_of1 import PortfolioAnalysisSharpeRatioPostRequestOneOf1
from openapi_client.models.portfolio_analysis_sharpe_ratio_post_request_one_of_portfolios_inner import PortfolioAnalysisSharpeRatioPostRequestOneOfPortfoliosInner
from openapi_client.models.portfolio_analysis_sharpe_ratio_probabilistic_minimum_track_record_length_post200_response import PortfolioAnalysisSharpeRatioProbabilisticMinimumTrackRecordLengthPost200Response
from openapi_client.models.portfolio_analysis_sharpe_ratio_probabilistic_minimum_track_record_length_post200_response_portfolios_inner import PortfolioAnalysisSharpeRatioProbabilisticMinimumTrackRecordLengthPost200ResponsePortfoliosInner
from openapi_client.models.portfolio_analysis_sharpe_ratio_probabilistic_minimum_track_record_length_post_request import PortfolioAnalysisSharpeRatioProbabilisticMinimumTrackRecordLengthPostRequest
from openapi_client.models.portfolio_analysis_sharpe_ratio_probabilistic_minimum_track_record_length_post_request_one_of import PortfolioAnalysisSharpeRatioProbabilisticMinimumTrackRecordLengthPostRequestOneOf
from openapi_client.models.portfolio_analysis_sharpe_ratio_probabilistic_minimum_track_record_length_post_request_one_of1 import PortfolioAnalysisSharpeRatioProbabilisticMinimumTrackRecordLengthPostRequestOneOf1
from openapi_client.models.portfolio_analysis_sharpe_ratio_probabilistic_post200_response import PortfolioAnalysisSharpeRatioProbabilisticPost200Response
from openapi_client.models.portfolio_analysis_sharpe_ratio_probabilistic_post200_response_portfolios_inner import PortfolioAnalysisSharpeRatioProbabilisticPost200ResponsePortfoliosInner
from openapi_client.models.portfolio_analysis_sharpe_ratio_probabilistic_post_request import PortfolioAnalysisSharpeRatioProbabilisticPostRequest
from openapi_client.models.portfolio_analysis_sharpe_ratio_probabilistic_post_request_one_of import PortfolioAnalysisSharpeRatioProbabilisticPostRequestOneOf
from openapi_client.models.portfolio_analysis_sharpe_ratio_probabilistic_post_request_one_of1 import PortfolioAnalysisSharpeRatioProbabilisticPostRequestOneOf1
from openapi_client.models.portfolio_analysis_sharpe_ratio_probabilistic_post_request_one_of1_portfolios_inner import PortfolioAnalysisSharpeRatioProbabilisticPostRequestOneOf1PortfoliosInner
from openapi_client.models.portfolio_analysis_tracking_error_post200_response import PortfolioAnalysisTrackingErrorPost200Response
from openapi_client.models.portfolio_analysis_tracking_error_post200_response_portfolios_inner import PortfolioAnalysisTrackingErrorPost200ResponsePortfoliosInner
from openapi_client.models.portfolio_analysis_tracking_error_post_request import PortfolioAnalysisTrackingErrorPostRequest
from openapi_client.models.portfolio_analysis_tracking_error_post_request_portfolios_inner import PortfolioAnalysisTrackingErrorPostRequestPortfoliosInner
from openapi_client.models.portfolio_analysis_ulcer_index_post200_response import PortfolioAnalysisUlcerIndexPost200Response
from openapi_client.models.portfolio_analysis_ulcer_index_post200_response_portfolios_inner import PortfolioAnalysisUlcerIndexPost200ResponsePortfoliosInner
from openapi_client.models.portfolio_analysis_ulcer_performance_index_post200_response import PortfolioAnalysisUlcerPerformanceIndexPost200Response
from openapi_client.models.portfolio_analysis_ulcer_performance_index_post200_response_portfolios_inner import PortfolioAnalysisUlcerPerformanceIndexPost200ResponsePortfoliosInner
from openapi_client.models.portfolio_analysis_value_at_risk_conditional_cornish_fisher_post200_response import PortfolioAnalysisValueAtRiskConditionalCornishFisherPost200Response
from openapi_client.models.portfolio_analysis_value_at_risk_conditional_cornish_fisher_post200_response_portfolios_inner import PortfolioAnalysisValueAtRiskConditionalCornishFisherPost200ResponsePortfoliosInner
from openapi_client.models.portfolio_analysis_value_at_risk_conditional_cornish_fisher_post_request import PortfolioAnalysisValueAtRiskConditionalCornishFisherPostRequest
from openapi_client.models.portfolio_analysis_value_at_risk_conditional_cornish_fisher_post_request_portfolios_inner import PortfolioAnalysisValueAtRiskConditionalCornishFisherPostRequestPortfoliosInner
from openapi_client.models.portfolio_analysis_value_at_risk_conditional_gaussian_post_request import PortfolioAnalysisValueAtRiskConditionalGaussianPostRequest
from openapi_client.models.portfolio_analysis_value_at_risk_conditional_gaussian_post_request_portfolios_inner import PortfolioAnalysisValueAtRiskConditionalGaussianPostRequestPortfoliosInner
from openapi_client.models.portfolio_analysis_value_at_risk_conditional_historical_post_request import PortfolioAnalysisValueAtRiskConditionalHistoricalPostRequest
from openapi_client.models.portfolio_analysis_value_at_risk_cornish_fisher_post200_response import PortfolioAnalysisValueAtRiskCornishFisherPost200Response
from openapi_client.models.portfolio_analysis_value_at_risk_cornish_fisher_post200_response_portfolios_inner import PortfolioAnalysisValueAtRiskCornishFisherPost200ResponsePortfoliosInner
from openapi_client.models.portfolio_analysis_volatility_post200_response import PortfolioAnalysisVolatilityPost200Response
from openapi_client.models.portfolio_analysis_volatility_post200_response_portfolios_inner import PortfolioAnalysisVolatilityPost200ResponsePortfoliosInner
from openapi_client.models.portfolio_analysis_volatility_post_request import PortfolioAnalysisVolatilityPostRequest
from openapi_client.models.portfolio_analysis_volatility_post_request_one_of import PortfolioAnalysisVolatilityPostRequestOneOf
from openapi_client.models.portfolio_construction_investable_post200_response import PortfolioConstructionInvestablePost200Response
from openapi_client.models.portfolio_construction_investable_post_request import PortfolioConstructionInvestablePostRequest
from openapi_client.models.portfolio_construction_mimicking_post_request import PortfolioConstructionMimickingPostRequest
from openapi_client.models.portfolio_construction_random_post200_response import PortfolioConstructionRandomPost200Response
from openapi_client.models.portfolio_construction_random_post_request import PortfolioConstructionRandomPostRequest
from openapi_client.models.portfolio_construction_random_post_request_constraints import PortfolioConstructionRandomPostRequestConstraints
from openapi_client.models.portfolio_optimization_equal_risk_contributions_post_request import PortfolioOptimizationEqualRiskContributionsPostRequest
from openapi_client.models.portfolio_optimization_equal_risk_contributions_post_request_constraints import PortfolioOptimizationEqualRiskContributionsPostRequestConstraints
from openapi_client.models.portfolio_optimization_equal_sharpe_ratio_contributions_post_request import PortfolioOptimizationEqualSharpeRatioContributionsPostRequest
from openapi_client.models.portfolio_optimization_equal_volatility_weighted_post_request import PortfolioOptimizationEqualVolatilityWeightedPostRequest
from openapi_client.models.portfolio_optimization_hierarchical_risk_parity_clustering_based_post_request import PortfolioOptimizationHierarchicalRiskParityClusteringBasedPostRequest
from openapi_client.models.portfolio_optimization_hierarchical_risk_parity_post_request import PortfolioOptimizationHierarchicalRiskParityPostRequest
from openapi_client.models.portfolio_optimization_inverse_variance_weighted_post_request import PortfolioOptimizationInverseVarianceWeightedPostRequest
from openapi_client.models.portfolio_optimization_market_capitalization_weighted_post_request import PortfolioOptimizationMarketCapitalizationWeightedPostRequest
from openapi_client.models.portfolio_optimization_maximum_decorrelation_post_request import PortfolioOptimizationMaximumDecorrelationPostRequest
from openapi_client.models.portfolio_optimization_maximum_return_diversified_post_request import PortfolioOptimizationMaximumReturnDiversifiedPostRequest
from openapi_client.models.portfolio_optimization_maximum_return_diversified_post_request_constraints import PortfolioOptimizationMaximumReturnDiversifiedPostRequestConstraints
from openapi_client.models.portfolio_optimization_maximum_return_post_request import PortfolioOptimizationMaximumReturnPostRequest
from openapi_client.models.portfolio_optimization_maximum_return_subset_resampling_based_post_request import PortfolioOptimizationMaximumReturnSubsetResamplingBasedPostRequest
from openapi_client.models.portfolio_optimization_maximum_sharpe_ratio_diversified_post_request import PortfolioOptimizationMaximumSharpeRatioDiversifiedPostRequest
from openapi_client.models.portfolio_optimization_maximum_sharpe_ratio_diversified_post_request_constraints import PortfolioOptimizationMaximumSharpeRatioDiversifiedPostRequestConstraints
from openapi_client.models.portfolio_optimization_maximum_sharpe_ratio_post_request import PortfolioOptimizationMaximumSharpeRatioPostRequest
from openapi_client.models.portfolio_optimization_maximum_sharpe_ratio_subset_resampling_based_post_request import PortfolioOptimizationMaximumSharpeRatioSubsetResamplingBasedPostRequest
from openapi_client.models.portfolio_optimization_maximum_ulcer_performance_index_post_request import PortfolioOptimizationMaximumUlcerPerformanceIndexPostRequest
from openapi_client.models.portfolio_optimization_mean_variance_efficient_diversified_post_request import PortfolioOptimizationMeanVarianceEfficientDiversifiedPostRequest
from openapi_client.models.portfolio_optimization_mean_variance_efficient_diversified_post_request_constraints import PortfolioOptimizationMeanVarianceEfficientDiversifiedPostRequestConstraints
from openapi_client.models.portfolio_optimization_mean_variance_efficient_post_request import PortfolioOptimizationMeanVarianceEfficientPostRequest
from openapi_client.models.portfolio_optimization_mean_variance_efficient_post_request_constraints import PortfolioOptimizationMeanVarianceEfficientPostRequestConstraints
from openapi_client.models.portfolio_optimization_mean_variance_efficient_subset_resampling_based_post_request import PortfolioOptimizationMeanVarianceEfficientSubsetResamplingBasedPostRequest
from openapi_client.models.portfolio_optimization_minimum_correlation_post_request import PortfolioOptimizationMinimumCorrelationPostRequest
from openapi_client.models.portfolio_optimization_minimum_ulcer_index_post_request import PortfolioOptimizationMinimumUlcerIndexPostRequest
from openapi_client.models.portfolio_optimization_minimum_variance_diversified_post_request import PortfolioOptimizationMinimumVarianceDiversifiedPostRequest
from openapi_client.models.portfolio_optimization_minimum_variance_diversified_post_request_constraints import PortfolioOptimizationMinimumVarianceDiversifiedPostRequestConstraints
from openapi_client.models.portfolio_optimization_minimum_variance_post_request import PortfolioOptimizationMinimumVariancePostRequest
from openapi_client.models.portfolio_optimization_minimum_variance_subset_resampling_based_post_request import PortfolioOptimizationMinimumVarianceSubsetResamplingBasedPostRequest
from openapi_client.models.portfolio_optimization_most_diversified_post_request import PortfolioOptimizationMostDiversifiedPostRequest
from openapi_client.models.portfolio_simulation_rebalancing_drift_weight_post200_response import PortfolioSimulationRebalancingDriftWeightPost200Response
from openapi_client.models.portfolio_simulation_rebalancing_drift_weight_post200_response_portfolios_inner import PortfolioSimulationRebalancingDriftWeightPost200ResponsePortfoliosInner
from openapi_client.models.portfolio_simulation_rebalancing_drift_weight_post_request import PortfolioSimulationRebalancingDriftWeightPostRequest
from openapi_client.models.portfolio_simulation_rebalancing_random_weight_post_request import PortfolioSimulationRebalancingRandomWeightPostRequest
