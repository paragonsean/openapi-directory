# BigQueryApi.TrainingOptions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activationFn** | **String** | Activation function of the neural nets. | [optional] 
**adjustStepChanges** | **Boolean** | If true, detect step changes and make data adjustment in the input time series. | [optional] 
**approxGlobalFeatureContrib** | **Boolean** | Whether to use approximate feature contribution method in XGBoost model explanation for global explain. | [optional] 
**autoArima** | **Boolean** | Whether to enable auto ARIMA or not. | [optional] 
**autoArimaMaxOrder** | **String** | The max value of the sum of non-seasonal p and q. | [optional] 
**autoArimaMinOrder** | **String** | The min value of the sum of non-seasonal p and q. | [optional] 
**autoClassWeights** | **Boolean** | Whether to calculate class weights automatically based on the popularity of each label. | [optional] 
**batchSize** | **String** | Batch size for dnn models. | [optional] 
**boosterType** | **String** | Booster type for boosted tree models. | [optional] 
**budgetHours** | **Number** | Budget in hours for AutoML training. | [optional] 
**calculatePValues** | **Boolean** | Whether or not p-value test should be computed for this model. Only available for linear and logistic regression models. | [optional] 
**categoryEncodingMethod** | **String** | Categorical feature encoding method. | [optional] 
**cleanSpikesAndDips** | **Boolean** | If true, clean spikes and dips in the input time series. | [optional] 
**colorSpace** | **String** | Enums for color space, used for processing images in Object Table. See more details at https://www.tensorflow.org/io/tutorials/colorspace. | [optional] 
**colsampleBylevel** | **Number** | Subsample ratio of columns for each level for boosted tree models. | [optional] 
**colsampleBynode** | **Number** | Subsample ratio of columns for each node(split) for boosted tree models. | [optional] 
**colsampleBytree** | **Number** | Subsample ratio of columns when constructing each tree for boosted tree models. | [optional] 
**dartNormalizeType** | **String** | Type of normalization algorithm for boosted tree models using dart booster. | [optional] 
**dataFrequency** | **String** | The data frequency of a time series. | [optional] 
**dataSplitColumn** | **String** | The column to split data with. This column won&#39;t be used as a feature. 1. When data_split_method is CUSTOM, the corresponding column should be boolean. The rows with true value tag are eval data, and the false are training data. 2. When data_split_method is SEQ, the first DATA_SPLIT_EVAL_FRACTION rows (from smallest to largest) in the corresponding column are used as training data, and the rest are eval data. It respects the order in Orderable data types: https://cloud.google.com/bigquery/docs/reference/standard-sql/data-types#data-type-properties | [optional] 
**dataSplitEvalFraction** | **Number** | The fraction of evaluation data over the whole input data. The rest of data will be used as training data. The format should be double. Accurate to two decimal places. Default value is 0.2. | [optional] 
**dataSplitMethod** | **String** | The data split type for training and evaluation, e.g. RANDOM. | [optional] 
**decomposeTimeSeries** | **Boolean** | If true, perform decompose time series and save the results. | [optional] 
**distanceType** | **String** | Distance type for clustering models. | [optional] 
**dropout** | **Number** | Dropout probability for dnn models. | [optional] 
**earlyStop** | **Boolean** | Whether to stop early when the loss doesn&#39;t improve significantly any more (compared to min_relative_progress). Used only for iterative training algorithms. | [optional] 
**enableGlobalExplain** | **Boolean** | If true, enable global explanation during training. | [optional] 
**feedbackType** | **String** | Feedback type that specifies which algorithm to run for matrix factorization. | [optional] 
**fitIntercept** | **Boolean** | Whether the model should include intercept during model training. | [optional] 
**hiddenUnits** | **[String]** | Hidden units for dnn models. | [optional] 
**holidayRegion** | **String** | The geographical region based on which the holidays are considered in time series modeling. If a valid value is specified, then holiday effects modeling is enabled. | [optional] 
**holidayRegions** | **[String]** | A list of geographical regions that are used for time series modeling. | [optional] 
**horizon** | **String** | The number of periods ahead that need to be forecasted. | [optional] 
**hparamTuningObjectives** | **[String]** | The target evaluation metrics to optimize the hyperparameters for. | [optional] 
**includeDrift** | **Boolean** | Include drift when fitting an ARIMA model. | [optional] 
**initialLearnRate** | **Number** | Specifies the initial learning rate for the line search learn rate strategy. | [optional] 
**inputLabelColumns** | **[String]** | Name of input label columns in training data. | [optional] 
**instanceWeightColumn** | **String** | Name of the instance weight column for training data. This column isn&#39;t be used as a feature. | [optional] 
**integratedGradientsNumSteps** | **String** | Number of integral steps for the integrated gradients explain method. | [optional] 
**itemColumn** | **String** | Item column specified for matrix factorization models. | [optional] 
**kmeansInitializationColumn** | **String** | The column used to provide the initial centroids for kmeans algorithm when kmeans_initialization_method is CUSTOM. | [optional] 
**kmeansInitializationMethod** | **String** | The method used to initialize the centroids for kmeans algorithm. | [optional] 
**l1RegActivation** | **Number** | L1 regularization coefficient to activations. | [optional] 
**l1Regularization** | **Number** | L1 regularization coefficient. | [optional] 
**l2Regularization** | **Number** | L2 regularization coefficient. | [optional] 
**labelClassWeights** | **{String: Number}** | Weights associated with each label class, for rebalancing the training data. Only applicable for classification models. | [optional] 
**learnRate** | **Number** | Learning rate in training. Used only for iterative training algorithms. | [optional] 
**learnRateStrategy** | **String** | The strategy to determine learn rate for the current iteration. | [optional] 
**lossType** | **String** | Type of loss function used during training run. | [optional] 
**maxIterations** | **String** | The maximum number of iterations in training. Used only for iterative training algorithms. | [optional] 
**maxParallelTrials** | **String** | Maximum number of trials to run in parallel. | [optional] 
**maxTimeSeriesLength** | **String** | The maximum number of time points in a time series that can be used in modeling the trend component of the time series. Don&#39;t use this option with the &#x60;timeSeriesLengthFraction&#x60; or &#x60;minTimeSeriesLength&#x60; options. | [optional] 
**maxTreeDepth** | **String** | Maximum depth of a tree for boosted tree models. | [optional] 
**minRelativeProgress** | **Number** | When early_stop is true, stops training when accuracy improvement is less than &#39;min_relative_progress&#39;. Used only for iterative training algorithms. | [optional] 
**minSplitLoss** | **Number** | Minimum split loss for boosted tree models. | [optional] 
**minTimeSeriesLength** | **String** | The minimum number of time points in a time series that are used in modeling the trend component of the time series. If you use this option you must also set the &#x60;timeSeriesLengthFraction&#x60; option. This training option ensures that enough time points are available when you use &#x60;timeSeriesLengthFraction&#x60; in trend modeling. This is particularly important when forecasting multiple time series in a single query using &#x60;timeSeriesIdColumn&#x60;. If the total number of time points is less than the &#x60;minTimeSeriesLength&#x60; value, then the query uses all available time points. | [optional] 
**minTreeChildWeight** | **String** | Minimum sum of instance weight needed in a child for boosted tree models. | [optional] 
**modelRegistry** | **String** | The model registry. | [optional] 
**modelUri** | **String** | Google Cloud Storage URI from which the model was imported. Only applicable for imported models. | [optional] 
**nonSeasonalOrder** | [**ArimaOrder**](ArimaOrder.md) |  | [optional] 
**numClusters** | **String** | Number of clusters for clustering models. | [optional] 
**numFactors** | **String** | Num factors specified for matrix factorization models. | [optional] 
**numParallelTree** | **String** | Number of parallel trees constructed during each iteration for boosted tree models. | [optional] 
**numPrincipalComponents** | **String** | Number of principal components to keep in the PCA model. Must be &lt;&#x3D; the number of features. | [optional] 
**numTrials** | **String** | Number of trials to run this hyperparameter tuning job. | [optional] 
**optimizationStrategy** | **String** | Optimization strategy for training linear regression models. | [optional] 
**optimizer** | **String** | Optimizer used for training the neural nets. | [optional] 
**pcaExplainedVarianceRatio** | **Number** | The minimum ratio of cumulative explained variance that needs to be given by the PCA model. | [optional] 
**pcaSolver** | **String** | The solver for PCA. | [optional] 
**sampledShapleyNumPaths** | **String** | Number of paths for the sampled Shapley explain method. | [optional] 
**scaleFeatures** | **Boolean** | If true, scale the feature values by dividing the feature standard deviation. Currently only apply to PCA. | [optional] 
**standardizeFeatures** | **Boolean** | Whether to standardize numerical features. Default to true. | [optional] 
**subsample** | **Number** | Subsample fraction of the training data to grow tree to prevent overfitting for boosted tree models. | [optional] 
**tfVersion** | **String** | Based on the selected TF version, the corresponding docker image is used to train external models. | [optional] 
**timeSeriesDataColumn** | **String** | Column to be designated as time series data for ARIMA model. | [optional] 
**timeSeriesIdColumn** | **String** | The time series id column that was used during ARIMA model training. | [optional] 
**timeSeriesIdColumns** | **[String]** | The time series id columns that were used during ARIMA model training. | [optional] 
**timeSeriesLengthFraction** | **Number** | The fraction of the interpolated length of the time series that&#39;s used to model the time series trend component. All of the time points of the time series are used to model the non-trend component. This training option accelerates modeling training without sacrificing much forecasting accuracy. You can use this option with &#x60;minTimeSeriesLength&#x60; but not with &#x60;maxTimeSeriesLength&#x60;. | [optional] 
**timeSeriesTimestampColumn** | **String** | Column to be designated as time series timestamp for ARIMA model. | [optional] 
**treeMethod** | **String** | Tree construction algorithm for boosted tree models. | [optional] 
**trendSmoothingWindowSize** | **String** | Smoothing window size for the trend component. When a positive value is specified, a center moving average smoothing is applied on the history trend. When the smoothing window is out of the boundary at the beginning or the end of the trend, the first element or the last element is padded to fill the smoothing window before the average is applied. | [optional] 
**userColumn** | **String** | User column specified for matrix factorization models. | [optional] 
**vertexAiModelVersionAliases** | **[String]** | The version aliases to apply in Vertex AI model registry. Always overwrite if the version aliases exists in a existing model. | [optional] 
**walsAlpha** | **Number** | Hyperparameter for matrix factoration when implicit feedback type is specified. | [optional] 
**warmStart** | **Boolean** | Whether to train a model from the last checkpoint. | [optional] 
**xgboostVersion** | **String** | User-selected XGBoost versions for training of XGBoost models. | [optional] 



## Enum: BoosterTypeEnum


* `BOOSTER_TYPE_UNSPECIFIED` (value: `"BOOSTER_TYPE_UNSPECIFIED"`)

* `GBTREE` (value: `"GBTREE"`)

* `DART` (value: `"DART"`)





## Enum: CategoryEncodingMethodEnum


* `ENCODING_METHOD_UNSPECIFIED` (value: `"ENCODING_METHOD_UNSPECIFIED"`)

* `ONE_HOT_ENCODING` (value: `"ONE_HOT_ENCODING"`)

* `LABEL_ENCODING` (value: `"LABEL_ENCODING"`)

* `DUMMY_ENCODING` (value: `"DUMMY_ENCODING"`)





## Enum: ColorSpaceEnum


* `COLOR_SPACE_UNSPECIFIED` (value: `"COLOR_SPACE_UNSPECIFIED"`)

* `RGB` (value: `"RGB"`)

* `HSV` (value: `"HSV"`)

* `YIQ` (value: `"YIQ"`)

* `YUV` (value: `"YUV"`)

* `GRAYSCALE` (value: `"GRAYSCALE"`)





## Enum: DartNormalizeTypeEnum


* `DART_NORMALIZE_TYPE_UNSPECIFIED` (value: `"DART_NORMALIZE_TYPE_UNSPECIFIED"`)

* `TREE` (value: `"TREE"`)

* `FOREST` (value: `"FOREST"`)





## Enum: DataFrequencyEnum


* `DATA_FREQUENCY_UNSPECIFIED` (value: `"DATA_FREQUENCY_UNSPECIFIED"`)

* `AUTO_FREQUENCY` (value: `"AUTO_FREQUENCY"`)

* `YEARLY` (value: `"YEARLY"`)

* `QUARTERLY` (value: `"QUARTERLY"`)

* `MONTHLY` (value: `"MONTHLY"`)

* `WEEKLY` (value: `"WEEKLY"`)

* `DAILY` (value: `"DAILY"`)

* `HOURLY` (value: `"HOURLY"`)

* `PER_MINUTE` (value: `"PER_MINUTE"`)





## Enum: DataSplitMethodEnum


* `DATA_SPLIT_METHOD_UNSPECIFIED` (value: `"DATA_SPLIT_METHOD_UNSPECIFIED"`)

* `RANDOM` (value: `"RANDOM"`)

* `CUSTOM` (value: `"CUSTOM"`)

* `SEQUENTIAL` (value: `"SEQUENTIAL"`)

* `NO_SPLIT` (value: `"NO_SPLIT"`)

* `AUTO_SPLIT` (value: `"AUTO_SPLIT"`)





## Enum: DistanceTypeEnum


* `DISTANCE_TYPE_UNSPECIFIED` (value: `"DISTANCE_TYPE_UNSPECIFIED"`)

* `EUCLIDEAN` (value: `"EUCLIDEAN"`)

* `COSINE` (value: `"COSINE"`)





## Enum: FeedbackTypeEnum


* `FEEDBACK_TYPE_UNSPECIFIED` (value: `"FEEDBACK_TYPE_UNSPECIFIED"`)

* `IMPLICIT` (value: `"IMPLICIT"`)

* `EXPLICIT` (value: `"EXPLICIT"`)





## Enum: HolidayRegionEnum


* `HOLIDAY_REGION_UNSPECIFIED` (value: `"HOLIDAY_REGION_UNSPECIFIED"`)

* `GLOBAL` (value: `"GLOBAL"`)

* `NA` (value: `"NA"`)

* `JAPAC` (value: `"JAPAC"`)

* `EMEA` (value: `"EMEA"`)

* `LAC` (value: `"LAC"`)

* `AE` (value: `"AE"`)

* `AR` (value: `"AR"`)

* `AT` (value: `"AT"`)

* `AU` (value: `"AU"`)

* `BE` (value: `"BE"`)

* `BR` (value: `"BR"`)

* `CA` (value: `"CA"`)

* `CH` (value: `"CH"`)

* `CL` (value: `"CL"`)

* `CN` (value: `"CN"`)

* `CO` (value: `"CO"`)

* `CS` (value: `"CS"`)

* `CZ` (value: `"CZ"`)

* `DE` (value: `"DE"`)

* `DK` (value: `"DK"`)

* `DZ` (value: `"DZ"`)

* `EC` (value: `"EC"`)

* `EE` (value: `"EE"`)

* `EG` (value: `"EG"`)

* `ES` (value: `"ES"`)

* `FI` (value: `"FI"`)

* `FR` (value: `"FR"`)

* `GB` (value: `"GB"`)

* `GR` (value: `"GR"`)

* `HK` (value: `"HK"`)

* `HU` (value: `"HU"`)

* `ID` (value: `"ID"`)

* `IE` (value: `"IE"`)

* `IL` (value: `"IL"`)

* `IN` (value: `"IN"`)

* `IR` (value: `"IR"`)

* `IT` (value: `"IT"`)

* `JP` (value: `"JP"`)

* `KR` (value: `"KR"`)

* `LV` (value: `"LV"`)

* `MA` (value: `"MA"`)

* `MX` (value: `"MX"`)

* `MY` (value: `"MY"`)

* `NG` (value: `"NG"`)

* `NL` (value: `"NL"`)

* `false` (value: `"false"`)

* `NZ` (value: `"NZ"`)

* `PE` (value: `"PE"`)

* `PH` (value: `"PH"`)

* `PK` (value: `"PK"`)

* `PL` (value: `"PL"`)

* `PT` (value: `"PT"`)

* `RO` (value: `"RO"`)

* `RS` (value: `"RS"`)

* `RU` (value: `"RU"`)

* `SA` (value: `"SA"`)

* `SE` (value: `"SE"`)

* `SG` (value: `"SG"`)

* `SI` (value: `"SI"`)

* `SK` (value: `"SK"`)

* `TH` (value: `"TH"`)

* `TR` (value: `"TR"`)

* `TW` (value: `"TW"`)

* `UA` (value: `"UA"`)

* `US` (value: `"US"`)

* `VE` (value: `"VE"`)

* `VN` (value: `"VN"`)

* `ZA` (value: `"ZA"`)





## Enum: [HolidayRegionsEnum]


* `HOLIDAY_REGION_UNSPECIFIED` (value: `"HOLIDAY_REGION_UNSPECIFIED"`)

* `GLOBAL` (value: `"GLOBAL"`)

* `NA` (value: `"NA"`)

* `JAPAC` (value: `"JAPAC"`)

* `EMEA` (value: `"EMEA"`)

* `LAC` (value: `"LAC"`)

* `AE` (value: `"AE"`)

* `AR` (value: `"AR"`)

* `AT` (value: `"AT"`)

* `AU` (value: `"AU"`)

* `BE` (value: `"BE"`)

* `BR` (value: `"BR"`)

* `CA` (value: `"CA"`)

* `CH` (value: `"CH"`)

* `CL` (value: `"CL"`)

* `CN` (value: `"CN"`)

* `CO` (value: `"CO"`)

* `CS` (value: `"CS"`)

* `CZ` (value: `"CZ"`)

* `DE` (value: `"DE"`)

* `DK` (value: `"DK"`)

* `DZ` (value: `"DZ"`)

* `EC` (value: `"EC"`)

* `EE` (value: `"EE"`)

* `EG` (value: `"EG"`)

* `ES` (value: `"ES"`)

* `FI` (value: `"FI"`)

* `FR` (value: `"FR"`)

* `GB` (value: `"GB"`)

* `GR` (value: `"GR"`)

* `HK` (value: `"HK"`)

* `HU` (value: `"HU"`)

* `ID` (value: `"ID"`)

* `IE` (value: `"IE"`)

* `IL` (value: `"IL"`)

* `IN` (value: `"IN"`)

* `IR` (value: `"IR"`)

* `IT` (value: `"IT"`)

* `JP` (value: `"JP"`)

* `KR` (value: `"KR"`)

* `LV` (value: `"LV"`)

* `MA` (value: `"MA"`)

* `MX` (value: `"MX"`)

* `MY` (value: `"MY"`)

* `NG` (value: `"NG"`)

* `NL` (value: `"NL"`)

* `false` (value: `"false"`)

* `NZ` (value: `"NZ"`)

* `PE` (value: `"PE"`)

* `PH` (value: `"PH"`)

* `PK` (value: `"PK"`)

* `PL` (value: `"PL"`)

* `PT` (value: `"PT"`)

* `RO` (value: `"RO"`)

* `RS` (value: `"RS"`)

* `RU` (value: `"RU"`)

* `SA` (value: `"SA"`)

* `SE` (value: `"SE"`)

* `SG` (value: `"SG"`)

* `SI` (value: `"SI"`)

* `SK` (value: `"SK"`)

* `TH` (value: `"TH"`)

* `TR` (value: `"TR"`)

* `TW` (value: `"TW"`)

* `UA` (value: `"UA"`)

* `US` (value: `"US"`)

* `VE` (value: `"VE"`)

* `VN` (value: `"VN"`)

* `ZA` (value: `"ZA"`)





## Enum: [HparamTuningObjectivesEnum]


* `HPARAM_TUNING_OBJECTIVE_UNSPECIFIED` (value: `"HPARAM_TUNING_OBJECTIVE_UNSPECIFIED"`)

* `MEAN_ABSOLUTE_ERROR` (value: `"MEAN_ABSOLUTE_ERROR"`)

* `MEAN_SQUARED_ERROR` (value: `"MEAN_SQUARED_ERROR"`)

* `MEAN_SQUARED_LOG_ERROR` (value: `"MEAN_SQUARED_LOG_ERROR"`)

* `MEDIAN_ABSOLUTE_ERROR` (value: `"MEDIAN_ABSOLUTE_ERROR"`)

* `R_SQUARED` (value: `"R_SQUARED"`)

* `EXPLAINED_VARIANCE` (value: `"EXPLAINED_VARIANCE"`)

* `PRECISION` (value: `"PRECISION"`)

* `RECALL` (value: `"RECALL"`)

* `ACCURACY` (value: `"ACCURACY"`)

* `F1_SCORE` (value: `"F1_SCORE"`)

* `LOG_LOSS` (value: `"LOG_LOSS"`)

* `ROC_AUC` (value: `"ROC_AUC"`)

* `DAVIES_BOULDIN_INDEX` (value: `"DAVIES_BOULDIN_INDEX"`)

* `MEAN_AVERAGE_PRECISION` (value: `"MEAN_AVERAGE_PRECISION"`)

* `NORMALIZED_DISCOUNTED_CUMULATIVE_GAIN` (value: `"NORMALIZED_DISCOUNTED_CUMULATIVE_GAIN"`)

* `AVERAGE_RANK` (value: `"AVERAGE_RANK"`)





## Enum: KmeansInitializationMethodEnum


* `KMEANS_INITIALIZATION_METHOD_UNSPECIFIED` (value: `"KMEANS_INITIALIZATION_METHOD_UNSPECIFIED"`)

* `RANDOM` (value: `"RANDOM"`)

* `CUSTOM` (value: `"CUSTOM"`)

* `KMEANS_PLUS_PLUS` (value: `"KMEANS_PLUS_PLUS"`)





## Enum: LearnRateStrategyEnum


* `LEARN_RATE_STRATEGY_UNSPECIFIED` (value: `"LEARN_RATE_STRATEGY_UNSPECIFIED"`)

* `LINE_SEARCH` (value: `"LINE_SEARCH"`)

* `CONSTANT` (value: `"CONSTANT"`)





## Enum: LossTypeEnum


* `LOSS_TYPE_UNSPECIFIED` (value: `"LOSS_TYPE_UNSPECIFIED"`)

* `MEAN_SQUARED_LOSS` (value: `"MEAN_SQUARED_LOSS"`)

* `MEAN_LOG_LOSS` (value: `"MEAN_LOG_LOSS"`)





## Enum: ModelRegistryEnum


* `MODEL_REGISTRY_UNSPECIFIED` (value: `"MODEL_REGISTRY_UNSPECIFIED"`)

* `VERTEX_AI` (value: `"VERTEX_AI"`)





## Enum: OptimizationStrategyEnum


* `OPTIMIZATION_STRATEGY_UNSPECIFIED` (value: `"OPTIMIZATION_STRATEGY_UNSPECIFIED"`)

* `BATCH_GRADIENT_DESCENT` (value: `"BATCH_GRADIENT_DESCENT"`)

* `NORMAL_EQUATION` (value: `"NORMAL_EQUATION"`)





## Enum: PcaSolverEnum


* `UNSPECIFIED` (value: `"UNSPECIFIED"`)

* `FULL` (value: `"FULL"`)

* `RANDOMIZED` (value: `"RANDOMIZED"`)

* `AUTO` (value: `"AUTO"`)





## Enum: TreeMethodEnum


* `TREE_METHOD_UNSPECIFIED` (value: `"TREE_METHOD_UNSPECIFIED"`)

* `AUTO` (value: `"AUTO"`)

* `EXACT` (value: `"EXACT"`)

* `APPROX` (value: `"APPROX"`)

* `HIST` (value: `"HIST"`)




