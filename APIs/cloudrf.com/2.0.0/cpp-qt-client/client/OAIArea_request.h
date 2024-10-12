/**
 * Cloud-RF API
 * Use this JSON API to build and test radio links for any radio, anywhere. Authenticate with your API2.0 key in the request header as key
 *
 * The version of the OpenAPI document: 2.0.0
 * Contact: support@cloudrf.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIArea_request.h
 *
 * 
 */

#ifndef OAIArea_request_H
#define OAIArea_request_H

#include <QJsonObject>

#include "OAIAntenna.h"
#include "OAIEnvironment.h"
#include "OAIModel.h"
#include "OAIOutput.h"
#include "OAIReceiver.h"
#include "OAITransmitter.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIAntenna;
class OAIEnvironment;
class OAIModel;
class OAIOutput;
class OAIReceiver;
class OAITransmitter;

class OAIArea_request : public OAIObject {
public:
    OAIArea_request();
    OAIArea_request(QString json);
    ~OAIArea_request() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIAntenna getAntenna() const;
    void setAntenna(const OAIAntenna &antenna);
    bool is_antenna_Set() const;
    bool is_antenna_Valid() const;

    OAIEnvironment getEnvironment() const;
    void setEnvironment(const OAIEnvironment &environment);
    bool is_environment_Set() const;
    bool is_environment_Valid() const;

    OAIModel getModel() const;
    void setModel(const OAIModel &model);
    bool is_model_Set() const;
    bool is_model_Valid() const;

    QString getNetwork() const;
    void setNetwork(const QString &network);
    bool is_network_Set() const;
    bool is_network_Valid() const;

    OAIOutput getOutput() const;
    void setOutput(const OAIOutput &output);
    bool is_output_Set() const;
    bool is_output_Valid() const;

    OAIReceiver getReceiver() const;
    void setReceiver(const OAIReceiver &receiver);
    bool is_receiver_Set() const;
    bool is_receiver_Valid() const;

    QString getSite() const;
    void setSite(const QString &site);
    bool is_site_Set() const;
    bool is_site_Valid() const;

    OAITransmitter getTransmitter() const;
    void setTransmitter(const OAITransmitter &transmitter);
    bool is_transmitter_Set() const;
    bool is_transmitter_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIAntenna m_antenna;
    bool m_antenna_isSet;
    bool m_antenna_isValid;

    OAIEnvironment m_environment;
    bool m_environment_isSet;
    bool m_environment_isValid;

    OAIModel m_model;
    bool m_model_isSet;
    bool m_model_isValid;

    QString m_network;
    bool m_network_isSet;
    bool m_network_isValid;

    OAIOutput m_output;
    bool m_output_isSet;
    bool m_output_isValid;

    OAIReceiver m_receiver;
    bool m_receiver_isSet;
    bool m_receiver_isValid;

    QString m_site;
    bool m_site_isSet;
    bool m_site_isValid;

    OAITransmitter m_transmitter;
    bool m_transmitter_isSet;
    bool m_transmitter_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIArea_request)

#endif // OAIArea_request_H
