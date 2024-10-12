

# TrainingOptions

Options used in model training.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**activationFn** | **String** | Activation function of the neural nets. |  [optional] |
|**adjustStepChanges** | **Boolean** | If true, detect step changes and make data adjustment in the input time series. |  [optional] |
|**approxGlobalFeatureContrib** | **Boolean** | Whether to use approximate feature contribution method in XGBoost model explanation for global explain. |  [optional] |
|**autoArima** | **Boolean** | Whether to enable auto ARIMA or not. |  [optional] |
|**autoArimaMaxOrder** | **String** | The max value of the sum of non-seasonal p and q. |  [optional] |
|**autoArimaMinOrder** | **String** | The min value of the sum of non-seasonal p and q. |  [optional] |
|**autoClassWeights** | **Boolean** | Whether to calculate class weights automatically based on the popularity of each label. |  [optional] |
|**batchSize** | **String** | Batch size for dnn models. |  [optional] |
|**boosterType** | [**BoosterTypeEnum**](#BoosterTypeEnum) | Booster type for boosted tree models. |  [optional] |
|**budgetHours** | **Double** | Budget in hours for AutoML training. |  [optional] |
|**calculatePValues** | **Boolean** | Whether or not p-value test should be computed for this model. Only available for linear and logistic regression models. |  [optional] |
|**categoryEncodingMethod** | [**CategoryEncodingMethodEnum**](#CategoryEncodingMethodEnum) | Categorical feature encoding method. |  [optional] |
|**cleanSpikesAndDips** | **Boolean** | If true, clean spikes and dips in the input time series. |  [optional] |
|**colorSpace** | [**ColorSpaceEnum**](#ColorSpaceEnum) | Enums for color space, used for processing images in Object Table. See more details at https://www.tensorflow.org/io/tutorials/colorspace. |  [optional] |
|**colsampleBylevel** | **Double** | Subsample ratio of columns for each level for boosted tree models. |  [optional] |
|**colsampleBynode** | **Double** | Subsample ratio of columns for each node(split) for boosted tree models. |  [optional] |
|**colsampleBytree** | **Double** | Subsample ratio of columns when constructing each tree for boosted tree models. |  [optional] |
|**dartNormalizeType** | [**DartNormalizeTypeEnum**](#DartNormalizeTypeEnum) | Type of normalization algorithm for boosted tree models using dart booster. |  [optional] |
|**dataFrequency** | [**DataFrequencyEnum**](#DataFrequencyEnum) | The data frequency of a time series. |  [optional] |
|**dataSplitColumn** | **String** | The column to split data with. This column won&#39;t be used as a feature. 1. When data_split_method is CUSTOM, the corresponding column should be boolean. The rows with true value tag are eval data, and the false are training data. 2. When data_split_method is SEQ, the first DATA_SPLIT_EVAL_FRACTION rows (from smallest to largest) in the corresponding column are used as training data, and the rest are eval data. It respects the order in Orderable data types: https://cloud.google.com/bigquery/docs/reference/standard-sql/data-types#data-type-properties |  [optional] |
|**dataSplitEvalFraction** | **Double** | The fraction of evaluation data over the whole input data. The rest of data will be used as training data. The format should be double. Accurate to two decimal places. Default value is 0.2. |  [optional] |
|**dataSplitMethod** | [**DataSplitMethodEnum**](#DataSplitMethodEnum) | The data split type for training and evaluation, e.g. RANDOM. |  [optional] |
|**decomposeTimeSeries** | **Boolean** | If true, perform decompose time series and save the results. |  [optional] |
|**distanceType** | [**DistanceTypeEnum**](#DistanceTypeEnum) | Distance type for clustering models. |  [optional] |
|**dropout** | **Double** | Dropout probability for dnn models. |  [optional] |
|**earlyStop** | **Boolean** | Whether to stop early when the loss doesn&#39;t improve significantly any more (compared to min_relative_progress). Used only for iterative training algorithms. |  [optional] |
|**enableGlobalExplain** | **Boolean** | If true, enable global explanation during training. |  [optional] |
|**feedbackType** | [**FeedbackTypeEnum**](#FeedbackTypeEnum) | Feedback type that specifies which algorithm to run for matrix factorization. |  [optional] |
|**fitIntercept** | **Boolean** | Whether the model should include intercept during model training. |  [optional] |
|**hiddenUnits** | **List&lt;String&gt;** | Hidden units for dnn models. |  [optional] |
|**holidayRegion** | [**HolidayRegionEnum**](#HolidayRegionEnum) | The geographical region based on which the holidays are considered in time series modeling. If a valid value is specified, then holiday effects modeling is enabled. |  [optional] |
|**holidayRegions** | [**List&lt;HolidayRegionsEnum&gt;**](#List&lt;HolidayRegionsEnum&gt;) | A list of geographical regions that are used for time series modeling. |  [optional] |
|**horizon** | **String** | The number of periods ahead that need to be forecasted. |  [optional] |
|**hparamTuningObjectives** | [**List&lt;HparamTuningObjectivesEnum&gt;**](#List&lt;HparamTuningObjectivesEnum&gt;) | The target evaluation metrics to optimize the hyperparameters for. |  [optional] |
|**includeDrift** | **Boolean** | Include drift when fitting an ARIMA model. |  [optional] |
|**initialLearnRate** | **Double** | Specifies the initial learning rate for the line search learn rate strategy. |  [optional] |
|**inputLabelColumns** | **List&lt;String&gt;** | Name of input label columns in training data. |  [optional] |
|**instanceWeightColumn** | **String** | Name of the instance weight column for training data. This column isn&#39;t be used as a feature. |  [optional] |
|**integratedGradientsNumSteps** | **String** | Number of integral steps for the integrated gradients explain method. |  [optional] |
|**itemColumn** | **String** | Item column specified for matrix factorization models. |  [optional] |
|**kmeansInitializationColumn** | **String** | The column used to provide the initial centroids for kmeans algorithm when kmeans_initialization_method is CUSTOM. |  [optional] |
|**kmeansInitializationMethod** | [**KmeansInitializationMethodEnum**](#KmeansInitializationMethodEnum) | The method used to initialize the centroids for kmeans algorithm. |  [optional] |
|**l1RegActivation** | **Double** | L1 regularization coefficient to activations. |  [optional] |
|**l1Regularization** | **Double** | L1 regularization coefficient. |  [optional] |
|**l2Regularization** | **Double** | L2 regularization coefficient. |  [optional] |
|**labelClassWeights** | **Map&lt;String, Double&gt;** | Weights associated with each label class, for rebalancing the training data. Only applicable for classification models. |  [optional] |
|**learnRate** | **Double** | Learning rate in training. Used only for iterative training algorithms. |  [optional] |
|**learnRateStrategy** | [**LearnRateStrategyEnum**](#LearnRateStrategyEnum) | The strategy to determine learn rate for the current iteration. |  [optional] |
|**lossType** | [**LossTypeEnum**](#LossTypeEnum) | Type of loss function used during training run. |  [optional] |
|**maxIterations** | **String** | The maximum number of iterations in training. Used only for iterative training algorithms. |  [optional] |
|**maxParallelTrials** | **String** | Maximum number of trials to run in parallel. |  [optional] |
|**maxTimeSeriesLength** | **String** | The maximum number of time points in a time series that can be used in modeling the trend component of the time series. Don&#39;t use this option with the &#x60;timeSeriesLengthFraction&#x60; or &#x60;minTimeSeriesLength&#x60; options. |  [optional] |
|**maxTreeDepth** | **String** | Maximum depth of a tree for boosted tree models. |  [optional] |
|**minRelativeProgress** | **Double** | When early_stop is true, stops training when accuracy improvement is less than &#39;min_relative_progress&#39;. Used only for iterative training algorithms. |  [optional] |
|**minSplitLoss** | **Double** | Minimum split loss for boosted tree models. |  [optional] |
|**minTimeSeriesLength** | **String** | The minimum number of time points in a time series that are used in modeling the trend component of the time series. If you use this option you must also set the &#x60;timeSeriesLengthFraction&#x60; option. This training option ensures that enough time points are available when you use &#x60;timeSeriesLengthFraction&#x60; in trend modeling. This is particularly important when forecasting multiple time series in a single query using &#x60;timeSeriesIdColumn&#x60;. If the total number of time points is less than the &#x60;minTimeSeriesLength&#x60; value, then the query uses all available time points. |  [optional] |
|**minTreeChildWeight** | **String** | Minimum sum of instance weight needed in a child for boosted tree models. |  [optional] |
|**modelRegistry** | [**ModelRegistryEnum**](#ModelRegistryEnum) | The model registry. |  [optional] |
|**modelUri** | **String** | Google Cloud Storage URI from which the model was imported. Only applicable for imported models. |  [optional] |
|**nonSeasonalOrder** | [**ArimaOrder**](ArimaOrder.md) |  |  [optional] |
|**numClusters** | **String** | Number of clusters for clustering models. |  [optional] |
|**numFactors** | **String** | Num factors specified for matrix factorization models. |  [optional] |
|**numParallelTree** | **String** | Number of parallel trees constructed during each iteration for boosted tree models. |  [optional] |
|**numPrincipalComponents** | **String** | Number of principal components to keep in the PCA model. Must be &lt;&#x3D; the number of features. |  [optional] |
|**numTrials** | **String** | Number of trials to run this hyperparameter tuning job. |  [optional] |
|**optimizationStrategy** | [**OptimizationStrategyEnum**](#OptimizationStrategyEnum) | Optimization strategy for training linear regression models. |  [optional] |
|**optimizer** | **String** | Optimizer used for training the neural nets. |  [optional] |
|**pcaExplainedVarianceRatio** | **Double** | The minimum ratio of cumulative explained variance that needs to be given by the PCA model. |  [optional] |
|**pcaSolver** | [**PcaSolverEnum**](#PcaSolverEnum) | The solver for PCA. |  [optional] |
|**sampledShapleyNumPaths** | **String** | Number of paths for the sampled Shapley explain method. |  [optional] |
|**scaleFeatures** | **Boolean** | If true, scale the feature values by dividing the feature standard deviation. Currently only apply to PCA. |  [optional] |
|**standardizeFeatures** | **Boolean** | Whether to standardize numerical features. Default to true. |  [optional] |
|**subsample** | **Double** | Subsample fraction of the training data to grow tree to prevent overfitting for boosted tree models. |  [optional] |
|**tfVersion** | **String** | Based on the selected TF version, the corresponding docker image is used to train external models. |  [optional] |
|**timeSeriesDataColumn** | **String** | Column to be designated as time series data for ARIMA model. |  [optional] |
|**timeSeriesIdColumn** | **String** | The time series id column that was used during ARIMA model training. |  [optional] |
|**timeSeriesIdColumns** | **List&lt;String&gt;** | The time series id columns that were used during ARIMA model training. |  [optional] |
|**timeSeriesLengthFraction** | **Double** | The fraction of the interpolated length of the time series that&#39;s used to model the time series trend component. All of the time points of the time series are used to model the non-trend component. This training option accelerates modeling training without sacrificing much forecasting accuracy. You can use this option with &#x60;minTimeSeriesLength&#x60; but not with &#x60;maxTimeSeriesLength&#x60;. |  [optional] |
|**timeSeriesTimestampColumn** | **String** | Column to be designated as time series timestamp for ARIMA model. |  [optional] |
|**treeMethod** | [**TreeMethodEnum**](#TreeMethodEnum) | Tree construction algorithm for boosted tree models. |  [optional] |
|**trendSmoothingWindowSize** | **String** | Smoothing window size for the trend component. When a positive value is specified, a center moving average smoothing is applied on the history trend. When the smoothing window is out of the boundary at the beginning or the end of the trend, the first element or the last element is padded to fill the smoothing window before the average is applied. |  [optional] |
|**userColumn** | **String** | User column specified for matrix factorization models. |  [optional] |
|**vertexAiModelVersionAliases** | **List&lt;String&gt;** | The version aliases to apply in Vertex AI model registry. Always overwrite if the version aliases exists in a existing model. |  [optional] |
|**walsAlpha** | **Double** | Hyperparameter for matrix factoration when implicit feedback type is specified. |  [optional] |
|**warmStart** | **Boolean** | Whether to train a model from the last checkpoint. |  [optional] |
|**xgboostVersion** | **String** | User-selected XGBoost versions for training of XGBoost models. |  [optional] |



## Enum: BoosterTypeEnum

| Name | Value |
|---- | -----|
| BOOSTER_TYPE_UNSPECIFIED | &quot;BOOSTER_TYPE_UNSPECIFIED&quot; |
| GBTREE | &quot;GBTREE&quot; |
| DART | &quot;DART&quot; |



## Enum: CategoryEncodingMethodEnum

| Name | Value |
|---- | -----|
| ENCODING_METHOD_UNSPECIFIED | &quot;ENCODING_METHOD_UNSPECIFIED&quot; |
| ONE_HOT_ENCODING | &quot;ONE_HOT_ENCODING&quot; |
| LABEL_ENCODING | &quot;LABEL_ENCODING&quot; |
| DUMMY_ENCODING | &quot;DUMMY_ENCODING&quot; |



## Enum: ColorSpaceEnum

| Name | Value |
|---- | -----|
| COLOR_SPACE_UNSPECIFIED | &quot;COLOR_SPACE_UNSPECIFIED&quot; |
| RGB | &quot;RGB&quot; |
| HSV | &quot;HSV&quot; |
| YIQ | &quot;YIQ&quot; |
| YUV | &quot;YUV&quot; |
| GRAYSCALE | &quot;GRAYSCALE&quot; |



## Enum: DartNormalizeTypeEnum

| Name | Value |
|---- | -----|
| DART_NORMALIZE_TYPE_UNSPECIFIED | &quot;DART_NORMALIZE_TYPE_UNSPECIFIED&quot; |
| TREE | &quot;TREE&quot; |
| FOREST | &quot;FOREST&quot; |



## Enum: DataFrequencyEnum

| Name | Value |
|---- | -----|
| DATA_FREQUENCY_UNSPECIFIED | &quot;DATA_FREQUENCY_UNSPECIFIED&quot; |
| AUTO_FREQUENCY | &quot;AUTO_FREQUENCY&quot; |
| YEARLY | &quot;YEARLY&quot; |
| QUARTERLY | &quot;QUARTERLY&quot; |
| MONTHLY | &quot;MONTHLY&quot; |
| WEEKLY | &quot;WEEKLY&quot; |
| DAILY | &quot;DAILY&quot; |
| HOURLY | &quot;HOURLY&quot; |
| PER_MINUTE | &quot;PER_MINUTE&quot; |



## Enum: DataSplitMethodEnum

| Name | Value |
|---- | -----|
| DATA_SPLIT_METHOD_UNSPECIFIED | &quot;DATA_SPLIT_METHOD_UNSPECIFIED&quot; |
| RANDOM | &quot;RANDOM&quot; |
| CUSTOM | &quot;CUSTOM&quot; |
| SEQUENTIAL | &quot;SEQUENTIAL&quot; |
| NO_SPLIT | &quot;NO_SPLIT&quot; |
| AUTO_SPLIT | &quot;AUTO_SPLIT&quot; |



## Enum: DistanceTypeEnum

| Name | Value |
|---- | -----|
| DISTANCE_TYPE_UNSPECIFIED | &quot;DISTANCE_TYPE_UNSPECIFIED&quot; |
| EUCLIDEAN | &quot;EUCLIDEAN&quot; |
| COSINE | &quot;COSINE&quot; |



## Enum: FeedbackTypeEnum

| Name | Value |
|---- | -----|
| FEEDBACK_TYPE_UNSPECIFIED | &quot;FEEDBACK_TYPE_UNSPECIFIED&quot; |
| IMPLICIT | &quot;IMPLICIT&quot; |
| EXPLICIT | &quot;EXPLICIT&quot; |



## Enum: HolidayRegionEnum

| Name | Value |
|---- | -----|
| HOLIDAY_REGION_UNSPECIFIED | &quot;HOLIDAY_REGION_UNSPECIFIED&quot; |
| GLOBAL | &quot;GLOBAL&quot; |
| NA | &quot;NA&quot; |
| JAPAC | &quot;JAPAC&quot; |
| EMEA | &quot;EMEA&quot; |
| LAC | &quot;LAC&quot; |
| AE | &quot;AE&quot; |
| AR | &quot;AR&quot; |
| AT | &quot;AT&quot; |
| AU | &quot;AU&quot; |
| BE | &quot;BE&quot; |
| BR | &quot;BR&quot; |
| CA | &quot;CA&quot; |
| CH | &quot;CH&quot; |
| CL | &quot;CL&quot; |
| CN | &quot;CN&quot; |
| CO | &quot;CO&quot; |
| CS | &quot;CS&quot; |
| CZ | &quot;CZ&quot; |
| DE | &quot;DE&quot; |
| DK | &quot;DK&quot; |
| DZ | &quot;DZ&quot; |
| EC | &quot;EC&quot; |
| EE | &quot;EE&quot; |
| EG | &quot;EG&quot; |
| ES | &quot;ES&quot; |
| FI | &quot;FI&quot; |
| FR | &quot;FR&quot; |
| GB | &quot;GB&quot; |
| GR | &quot;GR&quot; |
| HK | &quot;HK&quot; |
| HU | &quot;HU&quot; |
| ID | &quot;ID&quot; |
| IE | &quot;IE&quot; |
| IL | &quot;IL&quot; |
| IN | &quot;IN&quot; |
| IR | &quot;IR&quot; |
| IT | &quot;IT&quot; |
| JP | &quot;JP&quot; |
| KR | &quot;KR&quot; |
| LV | &quot;LV&quot; |
| MA | &quot;MA&quot; |
| MX | &quot;MX&quot; |
| MY | &quot;MY&quot; |
| NG | &quot;NG&quot; |
| NL | &quot;NL&quot; |
| FALSE | &quot;false&quot; |
| NZ | &quot;NZ&quot; |
| PE | &quot;PE&quot; |
| PH | &quot;PH&quot; |
| PK | &quot;PK&quot; |
| PL | &quot;PL&quot; |
| PT | &quot;PT&quot; |
| RO | &quot;RO&quot; |
| RS | &quot;RS&quot; |
| RU | &quot;RU&quot; |
| SA | &quot;SA&quot; |
| SE | &quot;SE&quot; |
| SG | &quot;SG&quot; |
| SI | &quot;SI&quot; |
| SK | &quot;SK&quot; |
| TH | &quot;TH&quot; |
| TR | &quot;TR&quot; |
| TW | &quot;TW&quot; |
| UA | &quot;UA&quot; |
| US | &quot;US&quot; |
| VE | &quot;VE&quot; |
| VN | &quot;VN&quot; |
| ZA | &quot;ZA&quot; |



## Enum: List&lt;HolidayRegionsEnum&gt;

| Name | Value |
|---- | -----|
| HOLIDAY_REGION_UNSPECIFIED | &quot;HOLIDAY_REGION_UNSPECIFIED&quot; |
| GLOBAL | &quot;GLOBAL&quot; |
| NA | &quot;NA&quot; |
| JAPAC | &quot;JAPAC&quot; |
| EMEA | &quot;EMEA&quot; |
| LAC | &quot;LAC&quot; |
| AE | &quot;AE&quot; |
| AR | &quot;AR&quot; |
| AT | &quot;AT&quot; |
| AU | &quot;AU&quot; |
| BE | &quot;BE&quot; |
| BR | &quot;BR&quot; |
| CA | &quot;CA&quot; |
| CH | &quot;CH&quot; |
| CL | &quot;CL&quot; |
| CN | &quot;CN&quot; |
| CO | &quot;CO&quot; |
| CS | &quot;CS&quot; |
| CZ | &quot;CZ&quot; |
| DE | &quot;DE&quot; |
| DK | &quot;DK&quot; |
| DZ | &quot;DZ&quot; |
| EC | &quot;EC&quot; |
| EE | &quot;EE&quot; |
| EG | &quot;EG&quot; |
| ES | &quot;ES&quot; |
| FI | &quot;FI&quot; |
| FR | &quot;FR&quot; |
| GB | &quot;GB&quot; |
| GR | &quot;GR&quot; |
| HK | &quot;HK&quot; |
| HU | &quot;HU&quot; |
| ID | &quot;ID&quot; |
| IE | &quot;IE&quot; |
| IL | &quot;IL&quot; |
| IN | &quot;IN&quot; |
| IR | &quot;IR&quot; |
| IT | &quot;IT&quot; |
| JP | &quot;JP&quot; |
| KR | &quot;KR&quot; |
| LV | &quot;LV&quot; |
| MA | &quot;MA&quot; |
| MX | &quot;MX&quot; |
| MY | &quot;MY&quot; |
| NG | &quot;NG&quot; |
| NL | &quot;NL&quot; |
| FALSE | &quot;false&quot; |
| NZ | &quot;NZ&quot; |
| PE | &quot;PE&quot; |
| PH | &quot;PH&quot; |
| PK | &quot;PK&quot; |
| PL | &quot;PL&quot; |
| PT | &quot;PT&quot; |
| RO | &quot;RO&quot; |
| RS | &quot;RS&quot; |
| RU | &quot;RU&quot; |
| SA | &quot;SA&quot; |
| SE | &quot;SE&quot; |
| SG | &quot;SG&quot; |
| SI | &quot;SI&quot; |
| SK | &quot;SK&quot; |
| TH | &quot;TH&quot; |
| TR | &quot;TR&quot; |
| TW | &quot;TW&quot; |
| UA | &quot;UA&quot; |
| US | &quot;US&quot; |
| VE | &quot;VE&quot; |
| VN | &quot;VN&quot; |
| ZA | &quot;ZA&quot; |



## Enum: List&lt;HparamTuningObjectivesEnum&gt;

| Name | Value |
|---- | -----|
| HPARAM_TUNING_OBJECTIVE_UNSPECIFIED | &quot;HPARAM_TUNING_OBJECTIVE_UNSPECIFIED&quot; |
| MEAN_ABSOLUTE_ERROR | &quot;MEAN_ABSOLUTE_ERROR&quot; |
| MEAN_SQUARED_ERROR | &quot;MEAN_SQUARED_ERROR&quot; |
| MEAN_SQUARED_LOG_ERROR | &quot;MEAN_SQUARED_LOG_ERROR&quot; |
| MEDIAN_ABSOLUTE_ERROR | &quot;MEDIAN_ABSOLUTE_ERROR&quot; |
| R_SQUARED | &quot;R_SQUARED&quot; |
| EXPLAINED_VARIANCE | &quot;EXPLAINED_VARIANCE&quot; |
| PRECISION | &quot;PRECISION&quot; |
| RECALL | &quot;RECALL&quot; |
| ACCURACY | &quot;ACCURACY&quot; |
| F1_SCORE | &quot;F1_SCORE&quot; |
| LOG_LOSS | &quot;LOG_LOSS&quot; |
| ROC_AUC | &quot;ROC_AUC&quot; |
| DAVIES_BOULDIN_INDEX | &quot;DAVIES_BOULDIN_INDEX&quot; |
| MEAN_AVERAGE_PRECISION | &quot;MEAN_AVERAGE_PRECISION&quot; |
| NORMALIZED_DISCOUNTED_CUMULATIVE_GAIN | &quot;NORMALIZED_DISCOUNTED_CUMULATIVE_GAIN&quot; |
| AVERAGE_RANK | &quot;AVERAGE_RANK&quot; |



## Enum: KmeansInitializationMethodEnum

| Name | Value |
|---- | -----|
| KMEANS_INITIALIZATION_METHOD_UNSPECIFIED | &quot;KMEANS_INITIALIZATION_METHOD_UNSPECIFIED&quot; |
| RANDOM | &quot;RANDOM&quot; |
| CUSTOM | &quot;CUSTOM&quot; |
| KMEANS_PLUS_PLUS | &quot;KMEANS_PLUS_PLUS&quot; |



## Enum: LearnRateStrategyEnum

| Name | Value |
|---- | -----|
| LEARN_RATE_STRATEGY_UNSPECIFIED | &quot;LEARN_RATE_STRATEGY_UNSPECIFIED&quot; |
| LINE_SEARCH | &quot;LINE_SEARCH&quot; |
| CONSTANT | &quot;CONSTANT&quot; |



## Enum: LossTypeEnum

| Name | Value |
|---- | -----|
| LOSS_TYPE_UNSPECIFIED | &quot;LOSS_TYPE_UNSPECIFIED&quot; |
| MEAN_SQUARED_LOSS | &quot;MEAN_SQUARED_LOSS&quot; |
| MEAN_LOG_LOSS | &quot;MEAN_LOG_LOSS&quot; |



## Enum: ModelRegistryEnum

| Name | Value |
|---- | -----|
| MODEL_REGISTRY_UNSPECIFIED | &quot;MODEL_REGISTRY_UNSPECIFIED&quot; |
| VERTEX_AI | &quot;VERTEX_AI&quot; |



## Enum: OptimizationStrategyEnum

| Name | Value |
|---- | -----|
| OPTIMIZATION_STRATEGY_UNSPECIFIED | &quot;OPTIMIZATION_STRATEGY_UNSPECIFIED&quot; |
| BATCH_GRADIENT_DESCENT | &quot;BATCH_GRADIENT_DESCENT&quot; |
| NORMAL_EQUATION | &quot;NORMAL_EQUATION&quot; |



## Enum: PcaSolverEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;UNSPECIFIED&quot; |
| FULL | &quot;FULL&quot; |
| RANDOMIZED | &quot;RANDOMIZED&quot; |
| AUTO | &quot;AUTO&quot; |



## Enum: TreeMethodEnum

| Name | Value |
|---- | -----|
| TREE_METHOD_UNSPECIFIED | &quot;TREE_METHOD_UNSPECIFIED&quot; |
| AUTO | &quot;AUTO&quot; |
| EXACT | &quot;EXACT&quot; |
| APPROX | &quot;APPROX&quot; |
| HIST | &quot;HIST&quot; |



