/**
 * AWS CodePipeline
 * <fullname>CodePipeline</fullname> <p> <b>Overview</b> </p> <p>This is the CodePipeline API Reference. This guide provides descriptions of the actions and data types for CodePipeline. Some functionality for your pipeline can only be configured through the API. For more information, see the <a href=\"https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html\">CodePipeline User Guide</a>.</p> <p>You can use the CodePipeline API to work with pipelines, stages, actions, and transitions.</p> <p> <i>Pipelines</i> are models of automated release processes. Each pipeline is uniquely named, and consists of stages, actions, and transitions. </p> <p>You can work with pipelines by calling:</p> <ul> <li> <p> <a>CreatePipeline</a>, which creates a uniquely named pipeline.</p> </li> <li> <p> <a>DeletePipeline</a>, which deletes the specified pipeline.</p> </li> <li> <p> <a>GetPipeline</a>, which returns information about the pipeline structure and pipeline metadata, including the pipeline Amazon Resource Name (ARN).</p> </li> <li> <p> <a>GetPipelineExecution</a>, which returns information about a specific execution of a pipeline.</p> </li> <li> <p> <a>GetPipelineState</a>, which returns information about the current state of the stages and actions of a pipeline.</p> </li> <li> <p> <a>ListActionExecutions</a>, which returns action-level details for past executions. The details include full stage and action-level details, including individual action duration, status, any errors that occurred during the execution, and input and output artifact location details.</p> </li> <li> <p> <a>ListPipelines</a>, which gets a summary of all of the pipelines associated with your account.</p> </li> <li> <p> <a>ListPipelineExecutions</a>, which gets a summary of the most recent executions for a pipeline.</p> </li> <li> <p> <a>StartPipelineExecution</a>, which runs the most recent revision of an artifact through the pipeline.</p> </li> <li> <p> <a>StopPipelineExecution</a>, which stops the specified pipeline execution from continuing through the pipeline.</p> </li> <li> <p> <a>UpdatePipeline</a>, which updates a pipeline with edits or changes to the structure of the pipeline.</p> </li> </ul> <p>Pipelines include <i>stages</i>. Each stage contains one or more actions that must complete before the next stage begins. A stage results in success or failure. If a stage fails, the pipeline stops at that stage and remains stopped until either a new version of an artifact appears in the source location, or a user takes action to rerun the most recent artifact through the pipeline. You can call <a>GetPipelineState</a>, which displays the status of a pipeline, including the status of stages in the pipeline, or <a>GetPipeline</a>, which returns the entire structure of the pipeline, including the stages of that pipeline. For more information about the structure of stages and actions, see <a href=\"https://docs.aws.amazon.com/codepipeline/latest/userguide/pipeline-structure.html\">CodePipeline Pipeline Structure Reference</a>.</p> <p>Pipeline stages include <i>actions</i> that are categorized into categories such as source or build actions performed in a stage of a pipeline. For example, you can use a source action to import artifacts into a pipeline from a source such as Amazon S3. Like stages, you do not work with actions directly in most cases, but you do define and interact with actions when working with pipeline operations such as <a>CreatePipeline</a> and <a>GetPipelineState</a>. Valid action categories are:</p> <ul> <li> <p>Source</p> </li> <li> <p>Build</p> </li> <li> <p>Test</p> </li> <li> <p>Deploy</p> </li> <li> <p>Approval</p> </li> <li> <p>Invoke</p> </li> </ul> <p>Pipelines also include <i>transitions</i>, which allow the transition of artifacts from one stage to the next in a pipeline after the actions in one stage complete.</p> <p>You can work with transitions by calling:</p> <ul> <li> <p> <a>DisableStageTransition</a>, which prevents artifacts from transitioning to the next stage in a pipeline.</p> </li> <li> <p> <a>EnableStageTransition</a>, which enables transition of artifacts between stages in a pipeline. </p> </li> </ul> <p> <b>Using the API to integrate with CodePipeline</b> </p> <p>For third-party integrators or developers who want to create their own integrations with CodePipeline, the expected sequence varies from the standard API user. To integrate with CodePipeline, developers need to work with the following items:</p> <p> <b>Jobs</b>, which are instances of an action. For example, a job for a source action might import a revision of an artifact from a source. </p> <p>You can work with jobs by calling:</p> <ul> <li> <p> <a>AcknowledgeJob</a>, which confirms whether a job worker has received the specified job.</p> </li> <li> <p> <a>GetJobDetails</a>, which returns the details of a job.</p> </li> <li> <p> <a>PollForJobs</a>, which determines whether there are any jobs to act on.</p> </li> <li> <p> <a>PutJobFailureResult</a>, which provides details of a job failure. </p> </li> <li> <p> <a>PutJobSuccessResult</a>, which provides details of a job success.</p> </li> </ul> <p> <b>Third party jobs</b>, which are instances of an action created by a partner action and integrated into CodePipeline. Partner actions are created by members of the Amazon Web Services Partner Network.</p> <p>You can work with third party jobs by calling:</p> <ul> <li> <p> <a>AcknowledgeThirdPartyJob</a>, which confirms whether a job worker has received the specified job.</p> </li> <li> <p> <a>GetThirdPartyJobDetails</a>, which requests the details of a job for a partner action.</p> </li> <li> <p> <a>PollForThirdPartyJobs</a>, which determines whether there are any jobs to act on. </p> </li> <li> <p> <a>PutThirdPartyJobFailureResult</a>, which provides details of a job failure.</p> </li> <li> <p> <a>PutThirdPartyJobSuccessResult</a>, which provides details of a job success.</p> </li> </ul>
 *
 * The version of the OpenAPI document: 2015-07-09
 * Contact: mike.ralphson@gmail.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAICreateCustomActionTypeInput_inputArtifactDetails.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICreateCustomActionTypeInput_inputArtifactDetails::OAICreateCustomActionTypeInput_inputArtifactDetails(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICreateCustomActionTypeInput_inputArtifactDetails::OAICreateCustomActionTypeInput_inputArtifactDetails() {
    this->initializeModel();
}

OAICreateCustomActionTypeInput_inputArtifactDetails::~OAICreateCustomActionTypeInput_inputArtifactDetails() {}

void OAICreateCustomActionTypeInput_inputArtifactDetails::initializeModel() {

    m_minimum_count_isSet = false;
    m_minimum_count_isValid = false;

    m_maximum_count_isSet = false;
    m_maximum_count_isValid = false;
}

void OAICreateCustomActionTypeInput_inputArtifactDetails::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICreateCustomActionTypeInput_inputArtifactDetails::fromJsonObject(QJsonObject json) {

    m_minimum_count_isValid = ::OpenAPI::fromJsonValue(m_minimum_count, json[QString("minimumCount")]);
    m_minimum_count_isSet = !json[QString("minimumCount")].isNull() && m_minimum_count_isValid;

    m_maximum_count_isValid = ::OpenAPI::fromJsonValue(m_maximum_count, json[QString("maximumCount")]);
    m_maximum_count_isSet = !json[QString("maximumCount")].isNull() && m_maximum_count_isValid;
}

QString OAICreateCustomActionTypeInput_inputArtifactDetails::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICreateCustomActionTypeInput_inputArtifactDetails::asJsonObject() const {
    QJsonObject obj;
    if (m_minimum_count_isSet) {
        obj.insert(QString("minimumCount"), ::OpenAPI::toJsonValue(m_minimum_count));
    }
    if (m_maximum_count_isSet) {
        obj.insert(QString("maximumCount"), ::OpenAPI::toJsonValue(m_maximum_count));
    }
    return obj;
}

qint32 OAICreateCustomActionTypeInput_inputArtifactDetails::getMinimumCount() const {
    return m_minimum_count;
}
void OAICreateCustomActionTypeInput_inputArtifactDetails::setMinimumCount(const qint32 &minimum_count) {
    m_minimum_count = minimum_count;
    m_minimum_count_isSet = true;
}

bool OAICreateCustomActionTypeInput_inputArtifactDetails::is_minimum_count_Set() const{
    return m_minimum_count_isSet;
}

bool OAICreateCustomActionTypeInput_inputArtifactDetails::is_minimum_count_Valid() const{
    return m_minimum_count_isValid;
}

qint32 OAICreateCustomActionTypeInput_inputArtifactDetails::getMaximumCount() const {
    return m_maximum_count;
}
void OAICreateCustomActionTypeInput_inputArtifactDetails::setMaximumCount(const qint32 &maximum_count) {
    m_maximum_count = maximum_count;
    m_maximum_count_isSet = true;
}

bool OAICreateCustomActionTypeInput_inputArtifactDetails::is_maximum_count_Set() const{
    return m_maximum_count_isSet;
}

bool OAICreateCustomActionTypeInput_inputArtifactDetails::is_maximum_count_Valid() const{
    return m_maximum_count_isValid;
}

bool OAICreateCustomActionTypeInput_inputArtifactDetails::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_minimum_count_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_maximum_count_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAICreateCustomActionTypeInput_inputArtifactDetails::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_minimum_count_isValid && m_maximum_count_isValid && true;
}

} // namespace OpenAPI
