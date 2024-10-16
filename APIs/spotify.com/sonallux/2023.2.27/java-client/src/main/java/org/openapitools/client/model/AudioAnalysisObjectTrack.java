/*
 * Spotify Web API with fixes and improvements from sonallux
 * You can use Spotify's Web API to discover music and podcasts, manage your Spotify library, control audio playback, and much more. Browse our available Web API endpoints using the sidebar at left, or via the navigation bar on top of this page on smaller screens.  In order to make successful Web API requests your app will need a valid access token. One can be obtained through <a href=\"https://developer.spotify.com/documentation/general/guides/authorization-guide/\">OAuth 2.0</a>.  The base URI for all Web API requests is `https://api.spotify.com/v1`.  Need help? See our <a href=\"https://developer.spotify.com/documentation/web-api/guides/\">Web API guides</a> for more information, or visit the <a href=\"https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer\">Spotify for Developers community forum</a> to ask questions and connect with other developers. 
 *
 * The version of the OpenAPI document: 2023.2.27
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.model;

import java.util.Objects;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import java.io.IOException;
import java.math.BigDecimal;
import java.util.Arrays;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.JsonArray;
import com.google.gson.JsonDeserializationContext;
import com.google.gson.JsonDeserializer;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.google.gson.JsonParseException;
import com.google.gson.TypeAdapterFactory;
import com.google.gson.reflect.TypeToken;
import com.google.gson.TypeAdapter;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import java.io.IOException;

import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

import org.openapitools.client.JSON;

/**
 * AudioAnalysisObjectTrack
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:05:56.088414-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class AudioAnalysisObjectTrack {
  public static final String SERIALIZED_NAME_ANALYSIS_CHANNELS = "analysis_channels";
  @SerializedName(SERIALIZED_NAME_ANALYSIS_CHANNELS)
  private Integer analysisChannels;

  public static final String SERIALIZED_NAME_ANALYSIS_SAMPLE_RATE = "analysis_sample_rate";
  @SerializedName(SERIALIZED_NAME_ANALYSIS_SAMPLE_RATE)
  private Integer analysisSampleRate;

  public static final String SERIALIZED_NAME_CODE_VERSION = "code_version";
  @SerializedName(SERIALIZED_NAME_CODE_VERSION)
  private BigDecimal codeVersion;

  public static final String SERIALIZED_NAME_CODESTRING = "codestring";
  @SerializedName(SERIALIZED_NAME_CODESTRING)
  private String codestring;

  public static final String SERIALIZED_NAME_DURATION = "duration";
  @SerializedName(SERIALIZED_NAME_DURATION)
  private BigDecimal duration;

  public static final String SERIALIZED_NAME_ECHOPRINT_VERSION = "echoprint_version";
  @SerializedName(SERIALIZED_NAME_ECHOPRINT_VERSION)
  private BigDecimal echoprintVersion;

  public static final String SERIALIZED_NAME_ECHOPRINTSTRING = "echoprintstring";
  @SerializedName(SERIALIZED_NAME_ECHOPRINTSTRING)
  private String echoprintstring;

  public static final String SERIALIZED_NAME_END_OF_FADE_IN = "end_of_fade_in";
  @SerializedName(SERIALIZED_NAME_END_OF_FADE_IN)
  private BigDecimal endOfFadeIn;

  public static final String SERIALIZED_NAME_KEY = "key";
  @SerializedName(SERIALIZED_NAME_KEY)
  private Integer key;

  public static final String SERIALIZED_NAME_KEY_CONFIDENCE = "key_confidence";
  @SerializedName(SERIALIZED_NAME_KEY_CONFIDENCE)
  private BigDecimal keyConfidence;

  public static final String SERIALIZED_NAME_LOUDNESS = "loudness";
  @SerializedName(SERIALIZED_NAME_LOUDNESS)
  private Float loudness;

  public static final String SERIALIZED_NAME_MODE = "mode";
  @SerializedName(SERIALIZED_NAME_MODE)
  private Integer mode;

  public static final String SERIALIZED_NAME_MODE_CONFIDENCE = "mode_confidence";
  @SerializedName(SERIALIZED_NAME_MODE_CONFIDENCE)
  private BigDecimal modeConfidence;

  public static final String SERIALIZED_NAME_NUM_SAMPLES = "num_samples";
  @SerializedName(SERIALIZED_NAME_NUM_SAMPLES)
  private Integer numSamples;

  public static final String SERIALIZED_NAME_OFFSET_SECONDS = "offset_seconds";
  @SerializedName(SERIALIZED_NAME_OFFSET_SECONDS)
  private Integer offsetSeconds;

  public static final String SERIALIZED_NAME_RHYTHM_VERSION = "rhythm_version";
  @SerializedName(SERIALIZED_NAME_RHYTHM_VERSION)
  private BigDecimal rhythmVersion;

  public static final String SERIALIZED_NAME_RHYTHMSTRING = "rhythmstring";
  @SerializedName(SERIALIZED_NAME_RHYTHMSTRING)
  private String rhythmstring;

  public static final String SERIALIZED_NAME_SAMPLE_MD5 = "sample_md5";
  @SerializedName(SERIALIZED_NAME_SAMPLE_MD5)
  private String sampleMd5;

  public static final String SERIALIZED_NAME_START_OF_FADE_OUT = "start_of_fade_out";
  @SerializedName(SERIALIZED_NAME_START_OF_FADE_OUT)
  private BigDecimal startOfFadeOut;

  public static final String SERIALIZED_NAME_SYNCH_VERSION = "synch_version";
  @SerializedName(SERIALIZED_NAME_SYNCH_VERSION)
  private BigDecimal synchVersion;

  public static final String SERIALIZED_NAME_SYNCHSTRING = "synchstring";
  @SerializedName(SERIALIZED_NAME_SYNCHSTRING)
  private String synchstring;

  public static final String SERIALIZED_NAME_TEMPO = "tempo";
  @SerializedName(SERIALIZED_NAME_TEMPO)
  private Float tempo;

  public static final String SERIALIZED_NAME_TEMPO_CONFIDENCE = "tempo_confidence";
  @SerializedName(SERIALIZED_NAME_TEMPO_CONFIDENCE)
  private BigDecimal tempoConfidence;

  public static final String SERIALIZED_NAME_TIME_SIGNATURE = "time_signature";
  @SerializedName(SERIALIZED_NAME_TIME_SIGNATURE)
  private Integer timeSignature;

  public static final String SERIALIZED_NAME_TIME_SIGNATURE_CONFIDENCE = "time_signature_confidence";
  @SerializedName(SERIALIZED_NAME_TIME_SIGNATURE_CONFIDENCE)
  private BigDecimal timeSignatureConfidence;

  public static final String SERIALIZED_NAME_WINDOW_SECONDS = "window_seconds";
  @SerializedName(SERIALIZED_NAME_WINDOW_SECONDS)
  private Integer windowSeconds;

  public AudioAnalysisObjectTrack() {
  }

  public AudioAnalysisObjectTrack analysisChannels(Integer analysisChannels) {
    this.analysisChannels = analysisChannels;
    return this;
  }

  /**
   * The number of channels used for analysis. If 1, all channels are summed together to mono before analysis.
   * @return analysisChannels
   */
  @javax.annotation.Nullable
  public Integer getAnalysisChannels() {
    return analysisChannels;
  }

  public void setAnalysisChannels(Integer analysisChannels) {
    this.analysisChannels = analysisChannels;
  }


  public AudioAnalysisObjectTrack analysisSampleRate(Integer analysisSampleRate) {
    this.analysisSampleRate = analysisSampleRate;
    return this;
  }

  /**
   * The sample rate used to decode and analyze this track. May differ from the actual sample rate of this track available on Spotify.
   * @return analysisSampleRate
   */
  @javax.annotation.Nullable
  public Integer getAnalysisSampleRate() {
    return analysisSampleRate;
  }

  public void setAnalysisSampleRate(Integer analysisSampleRate) {
    this.analysisSampleRate = analysisSampleRate;
  }


  public AudioAnalysisObjectTrack codeVersion(BigDecimal codeVersion) {
    this.codeVersion = codeVersion;
    return this;
  }

  /**
   * A version number for the Echo Nest Musical Fingerprint format used in the codestring field.
   * @return codeVersion
   */
  @javax.annotation.Nullable
  public BigDecimal getCodeVersion() {
    return codeVersion;
  }

  public void setCodeVersion(BigDecimal codeVersion) {
    this.codeVersion = codeVersion;
  }


  public AudioAnalysisObjectTrack codestring(String codestring) {
    this.codestring = codestring;
    return this;
  }

  /**
   * An [Echo Nest Musical Fingerprint (ENMFP)](https://academiccommons.columbia.edu/doi/10.7916/D8Q248M4) codestring for this track.
   * @return codestring
   */
  @javax.annotation.Nullable
  public String getCodestring() {
    return codestring;
  }

  public void setCodestring(String codestring) {
    this.codestring = codestring;
  }


  public AudioAnalysisObjectTrack duration(BigDecimal duration) {
    this.duration = duration;
    return this;
  }

  /**
   * Length of the track in seconds.
   * @return duration
   */
  @javax.annotation.Nullable
  public BigDecimal getDuration() {
    return duration;
  }

  public void setDuration(BigDecimal duration) {
    this.duration = duration;
  }


  public AudioAnalysisObjectTrack echoprintVersion(BigDecimal echoprintVersion) {
    this.echoprintVersion = echoprintVersion;
    return this;
  }

  /**
   * A version number for the EchoPrint format used in the echoprintstring field.
   * @return echoprintVersion
   */
  @javax.annotation.Nullable
  public BigDecimal getEchoprintVersion() {
    return echoprintVersion;
  }

  public void setEchoprintVersion(BigDecimal echoprintVersion) {
    this.echoprintVersion = echoprintVersion;
  }


  public AudioAnalysisObjectTrack echoprintstring(String echoprintstring) {
    this.echoprintstring = echoprintstring;
    return this;
  }

  /**
   * An [EchoPrint](https://github.com/spotify/echoprint-codegen) codestring for this track.
   * @return echoprintstring
   */
  @javax.annotation.Nullable
  public String getEchoprintstring() {
    return echoprintstring;
  }

  public void setEchoprintstring(String echoprintstring) {
    this.echoprintstring = echoprintstring;
  }


  public AudioAnalysisObjectTrack endOfFadeIn(BigDecimal endOfFadeIn) {
    this.endOfFadeIn = endOfFadeIn;
    return this;
  }

  /**
   * The time, in seconds, at which the track&#39;s fade-in period ends. If the track has no fade-in, this will be 0.0.
   * @return endOfFadeIn
   */
  @javax.annotation.Nullable
  public BigDecimal getEndOfFadeIn() {
    return endOfFadeIn;
  }

  public void setEndOfFadeIn(BigDecimal endOfFadeIn) {
    this.endOfFadeIn = endOfFadeIn;
  }


  public AudioAnalysisObjectTrack key(Integer key) {
    this.key = key;
    return this;
  }

  /**
   * The key the track is in. Integers map to pitches using standard [Pitch Class notation](https://en.wikipedia.org/wiki/Pitch_class). E.g. 0 &#x3D; C, 1 &#x3D; C♯/D♭, 2 &#x3D; D, and so on. If no key was detected, the value is -1. 
   * minimum: -1
   * maximum: 11
   * @return key
   */
  @javax.annotation.Nullable
  public Integer getKey() {
    return key;
  }

  public void setKey(Integer key) {
    this.key = key;
  }


  public AudioAnalysisObjectTrack keyConfidence(BigDecimal keyConfidence) {
    this.keyConfidence = keyConfidence;
    return this;
  }

  /**
   * The confidence, from 0.0 to 1.0, of the reliability of the &#x60;key&#x60;.
   * minimum: 0
   * maximum: 1
   * @return keyConfidence
   */
  @javax.annotation.Nullable
  public BigDecimal getKeyConfidence() {
    return keyConfidence;
  }

  public void setKeyConfidence(BigDecimal keyConfidence) {
    this.keyConfidence = keyConfidence;
  }


  public AudioAnalysisObjectTrack loudness(Float loudness) {
    this.loudness = loudness;
    return this;
  }

  /**
   * The overall loudness of a track in decibels (dB). Loudness values are averaged across the entire track and are useful for comparing relative loudness of tracks. Loudness is the quality of a sound that is the primary psychological correlate of physical strength (amplitude). Values typically range between -60 and 0 db. 
   * @return loudness
   */
  @javax.annotation.Nullable
  public Float getLoudness() {
    return loudness;
  }

  public void setLoudness(Float loudness) {
    this.loudness = loudness;
  }


  public AudioAnalysisObjectTrack mode(Integer mode) {
    this.mode = mode;
    return this;
  }

  /**
   * Mode indicates the modality (major or minor) of a track, the type of scale from which its melodic content is derived. Major is represented by 1 and minor is 0. 
   * @return mode
   */
  @javax.annotation.Nullable
  public Integer getMode() {
    return mode;
  }

  public void setMode(Integer mode) {
    this.mode = mode;
  }


  public AudioAnalysisObjectTrack modeConfidence(BigDecimal modeConfidence) {
    this.modeConfidence = modeConfidence;
    return this;
  }

  /**
   * The confidence, from 0.0 to 1.0, of the reliability of the &#x60;mode&#x60;.
   * minimum: 0
   * maximum: 1
   * @return modeConfidence
   */
  @javax.annotation.Nullable
  public BigDecimal getModeConfidence() {
    return modeConfidence;
  }

  public void setModeConfidence(BigDecimal modeConfidence) {
    this.modeConfidence = modeConfidence;
  }


  public AudioAnalysisObjectTrack numSamples(Integer numSamples) {
    this.numSamples = numSamples;
    return this;
  }

  /**
   * The exact number of audio samples analyzed from this track. See also &#x60;analysis_sample_rate&#x60;.
   * @return numSamples
   */
  @javax.annotation.Nullable
  public Integer getNumSamples() {
    return numSamples;
  }

  public void setNumSamples(Integer numSamples) {
    this.numSamples = numSamples;
  }


  public AudioAnalysisObjectTrack offsetSeconds(Integer offsetSeconds) {
    this.offsetSeconds = offsetSeconds;
    return this;
  }

  /**
   * An offset to the start of the region of the track that was analyzed. (As the entire track is analyzed, this should always be 0.)
   * @return offsetSeconds
   */
  @javax.annotation.Nullable
  public Integer getOffsetSeconds() {
    return offsetSeconds;
  }

  public void setOffsetSeconds(Integer offsetSeconds) {
    this.offsetSeconds = offsetSeconds;
  }


  public AudioAnalysisObjectTrack rhythmVersion(BigDecimal rhythmVersion) {
    this.rhythmVersion = rhythmVersion;
    return this;
  }

  /**
   * A version number for the Rhythmstring used in the rhythmstring field.
   * @return rhythmVersion
   */
  @javax.annotation.Nullable
  public BigDecimal getRhythmVersion() {
    return rhythmVersion;
  }

  public void setRhythmVersion(BigDecimal rhythmVersion) {
    this.rhythmVersion = rhythmVersion;
  }


  public AudioAnalysisObjectTrack rhythmstring(String rhythmstring) {
    this.rhythmstring = rhythmstring;
    return this;
  }

  /**
   * A Rhythmstring for this track. The format of this string is similar to the Synchstring.
   * @return rhythmstring
   */
  @javax.annotation.Nullable
  public String getRhythmstring() {
    return rhythmstring;
  }

  public void setRhythmstring(String rhythmstring) {
    this.rhythmstring = rhythmstring;
  }


  public AudioAnalysisObjectTrack sampleMd5(String sampleMd5) {
    this.sampleMd5 = sampleMd5;
    return this;
  }

  /**
   * This field will always contain the empty string.
   * @return sampleMd5
   */
  @javax.annotation.Nullable
  public String getSampleMd5() {
    return sampleMd5;
  }

  public void setSampleMd5(String sampleMd5) {
    this.sampleMd5 = sampleMd5;
  }


  public AudioAnalysisObjectTrack startOfFadeOut(BigDecimal startOfFadeOut) {
    this.startOfFadeOut = startOfFadeOut;
    return this;
  }

  /**
   * The time, in seconds, at which the track&#39;s fade-out period starts. If the track has no fade-out, this should match the track&#39;s length.
   * @return startOfFadeOut
   */
  @javax.annotation.Nullable
  public BigDecimal getStartOfFadeOut() {
    return startOfFadeOut;
  }

  public void setStartOfFadeOut(BigDecimal startOfFadeOut) {
    this.startOfFadeOut = startOfFadeOut;
  }


  public AudioAnalysisObjectTrack synchVersion(BigDecimal synchVersion) {
    this.synchVersion = synchVersion;
    return this;
  }

  /**
   * A version number for the Synchstring used in the synchstring field.
   * @return synchVersion
   */
  @javax.annotation.Nullable
  public BigDecimal getSynchVersion() {
    return synchVersion;
  }

  public void setSynchVersion(BigDecimal synchVersion) {
    this.synchVersion = synchVersion;
  }


  public AudioAnalysisObjectTrack synchstring(String synchstring) {
    this.synchstring = synchstring;
    return this;
  }

  /**
   * A [Synchstring](https://github.com/echonest/synchdata) for this track.
   * @return synchstring
   */
  @javax.annotation.Nullable
  public String getSynchstring() {
    return synchstring;
  }

  public void setSynchstring(String synchstring) {
    this.synchstring = synchstring;
  }


  public AudioAnalysisObjectTrack tempo(Float tempo) {
    this.tempo = tempo;
    return this;
  }

  /**
   * The overall estimated tempo of a track in beats per minute (BPM). In musical terminology, tempo is the speed or pace of a given piece and derives directly from the average beat duration. 
   * @return tempo
   */
  @javax.annotation.Nullable
  public Float getTempo() {
    return tempo;
  }

  public void setTempo(Float tempo) {
    this.tempo = tempo;
  }


  public AudioAnalysisObjectTrack tempoConfidence(BigDecimal tempoConfidence) {
    this.tempoConfidence = tempoConfidence;
    return this;
  }

  /**
   * The confidence, from 0.0 to 1.0, of the reliability of the &#x60;tempo&#x60;.
   * minimum: 0
   * maximum: 1
   * @return tempoConfidence
   */
  @javax.annotation.Nullable
  public BigDecimal getTempoConfidence() {
    return tempoConfidence;
  }

  public void setTempoConfidence(BigDecimal tempoConfidence) {
    this.tempoConfidence = tempoConfidence;
  }


  public AudioAnalysisObjectTrack timeSignature(Integer timeSignature) {
    this.timeSignature = timeSignature;
    return this;
  }

  /**
   * An estimated time signature. The time signature (meter) is a notational convention to specify how many beats are in each bar (or measure). The time signature ranges from 3 to 7 indicating time signatures of \&quot;3/4\&quot;, to \&quot;7/4\&quot;.
   * minimum: 3
   * maximum: 7
   * @return timeSignature
   */
  @javax.annotation.Nullable
  public Integer getTimeSignature() {
    return timeSignature;
  }

  public void setTimeSignature(Integer timeSignature) {
    this.timeSignature = timeSignature;
  }


  public AudioAnalysisObjectTrack timeSignatureConfidence(BigDecimal timeSignatureConfidence) {
    this.timeSignatureConfidence = timeSignatureConfidence;
    return this;
  }

  /**
   * The confidence, from 0.0 to 1.0, of the reliability of the &#x60;time_signature&#x60;.
   * minimum: 0
   * maximum: 1
   * @return timeSignatureConfidence
   */
  @javax.annotation.Nullable
  public BigDecimal getTimeSignatureConfidence() {
    return timeSignatureConfidence;
  }

  public void setTimeSignatureConfidence(BigDecimal timeSignatureConfidence) {
    this.timeSignatureConfidence = timeSignatureConfidence;
  }


  public AudioAnalysisObjectTrack windowSeconds(Integer windowSeconds) {
    this.windowSeconds = windowSeconds;
    return this;
  }

  /**
   * The length of the region of the track was analyzed, if a subset of the track was analyzed. (As the entire track is analyzed, this should always be 0.)
   * @return windowSeconds
   */
  @javax.annotation.Nullable
  public Integer getWindowSeconds() {
    return windowSeconds;
  }

  public void setWindowSeconds(Integer windowSeconds) {
    this.windowSeconds = windowSeconds;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    AudioAnalysisObjectTrack audioAnalysisObjectTrack = (AudioAnalysisObjectTrack) o;
    return Objects.equals(this.analysisChannels, audioAnalysisObjectTrack.analysisChannels) &&
        Objects.equals(this.analysisSampleRate, audioAnalysisObjectTrack.analysisSampleRate) &&
        Objects.equals(this.codeVersion, audioAnalysisObjectTrack.codeVersion) &&
        Objects.equals(this.codestring, audioAnalysisObjectTrack.codestring) &&
        Objects.equals(this.duration, audioAnalysisObjectTrack.duration) &&
        Objects.equals(this.echoprintVersion, audioAnalysisObjectTrack.echoprintVersion) &&
        Objects.equals(this.echoprintstring, audioAnalysisObjectTrack.echoprintstring) &&
        Objects.equals(this.endOfFadeIn, audioAnalysisObjectTrack.endOfFadeIn) &&
        Objects.equals(this.key, audioAnalysisObjectTrack.key) &&
        Objects.equals(this.keyConfidence, audioAnalysisObjectTrack.keyConfidence) &&
        Objects.equals(this.loudness, audioAnalysisObjectTrack.loudness) &&
        Objects.equals(this.mode, audioAnalysisObjectTrack.mode) &&
        Objects.equals(this.modeConfidence, audioAnalysisObjectTrack.modeConfidence) &&
        Objects.equals(this.numSamples, audioAnalysisObjectTrack.numSamples) &&
        Objects.equals(this.offsetSeconds, audioAnalysisObjectTrack.offsetSeconds) &&
        Objects.equals(this.rhythmVersion, audioAnalysisObjectTrack.rhythmVersion) &&
        Objects.equals(this.rhythmstring, audioAnalysisObjectTrack.rhythmstring) &&
        Objects.equals(this.sampleMd5, audioAnalysisObjectTrack.sampleMd5) &&
        Objects.equals(this.startOfFadeOut, audioAnalysisObjectTrack.startOfFadeOut) &&
        Objects.equals(this.synchVersion, audioAnalysisObjectTrack.synchVersion) &&
        Objects.equals(this.synchstring, audioAnalysisObjectTrack.synchstring) &&
        Objects.equals(this.tempo, audioAnalysisObjectTrack.tempo) &&
        Objects.equals(this.tempoConfidence, audioAnalysisObjectTrack.tempoConfidence) &&
        Objects.equals(this.timeSignature, audioAnalysisObjectTrack.timeSignature) &&
        Objects.equals(this.timeSignatureConfidence, audioAnalysisObjectTrack.timeSignatureConfidence) &&
        Objects.equals(this.windowSeconds, audioAnalysisObjectTrack.windowSeconds);
  }

  @Override
  public int hashCode() {
    return Objects.hash(analysisChannels, analysisSampleRate, codeVersion, codestring, duration, echoprintVersion, echoprintstring, endOfFadeIn, key, keyConfidence, loudness, mode, modeConfidence, numSamples, offsetSeconds, rhythmVersion, rhythmstring, sampleMd5, startOfFadeOut, synchVersion, synchstring, tempo, tempoConfidence, timeSignature, timeSignatureConfidence, windowSeconds);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class AudioAnalysisObjectTrack {\n");
    sb.append("    analysisChannels: ").append(toIndentedString(analysisChannels)).append("\n");
    sb.append("    analysisSampleRate: ").append(toIndentedString(analysisSampleRate)).append("\n");
    sb.append("    codeVersion: ").append(toIndentedString(codeVersion)).append("\n");
    sb.append("    codestring: ").append(toIndentedString(codestring)).append("\n");
    sb.append("    duration: ").append(toIndentedString(duration)).append("\n");
    sb.append("    echoprintVersion: ").append(toIndentedString(echoprintVersion)).append("\n");
    sb.append("    echoprintstring: ").append(toIndentedString(echoprintstring)).append("\n");
    sb.append("    endOfFadeIn: ").append(toIndentedString(endOfFadeIn)).append("\n");
    sb.append("    key: ").append(toIndentedString(key)).append("\n");
    sb.append("    keyConfidence: ").append(toIndentedString(keyConfidence)).append("\n");
    sb.append("    loudness: ").append(toIndentedString(loudness)).append("\n");
    sb.append("    mode: ").append(toIndentedString(mode)).append("\n");
    sb.append("    modeConfidence: ").append(toIndentedString(modeConfidence)).append("\n");
    sb.append("    numSamples: ").append(toIndentedString(numSamples)).append("\n");
    sb.append("    offsetSeconds: ").append(toIndentedString(offsetSeconds)).append("\n");
    sb.append("    rhythmVersion: ").append(toIndentedString(rhythmVersion)).append("\n");
    sb.append("    rhythmstring: ").append(toIndentedString(rhythmstring)).append("\n");
    sb.append("    sampleMd5: ").append(toIndentedString(sampleMd5)).append("\n");
    sb.append("    startOfFadeOut: ").append(toIndentedString(startOfFadeOut)).append("\n");
    sb.append("    synchVersion: ").append(toIndentedString(synchVersion)).append("\n");
    sb.append("    synchstring: ").append(toIndentedString(synchstring)).append("\n");
    sb.append("    tempo: ").append(toIndentedString(tempo)).append("\n");
    sb.append("    tempoConfidence: ").append(toIndentedString(tempoConfidence)).append("\n");
    sb.append("    timeSignature: ").append(toIndentedString(timeSignature)).append("\n");
    sb.append("    timeSignatureConfidence: ").append(toIndentedString(timeSignatureConfidence)).append("\n");
    sb.append("    windowSeconds: ").append(toIndentedString(windowSeconds)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }


  public static HashSet<String> openapiFields;
  public static HashSet<String> openapiRequiredFields;

  static {
    // a set of all properties/fields (JSON key names)
    openapiFields = new HashSet<String>();
    openapiFields.add("analysis_channels");
    openapiFields.add("analysis_sample_rate");
    openapiFields.add("code_version");
    openapiFields.add("codestring");
    openapiFields.add("duration");
    openapiFields.add("echoprint_version");
    openapiFields.add("echoprintstring");
    openapiFields.add("end_of_fade_in");
    openapiFields.add("key");
    openapiFields.add("key_confidence");
    openapiFields.add("loudness");
    openapiFields.add("mode");
    openapiFields.add("mode_confidence");
    openapiFields.add("num_samples");
    openapiFields.add("offset_seconds");
    openapiFields.add("rhythm_version");
    openapiFields.add("rhythmstring");
    openapiFields.add("sample_md5");
    openapiFields.add("start_of_fade_out");
    openapiFields.add("synch_version");
    openapiFields.add("synchstring");
    openapiFields.add("tempo");
    openapiFields.add("tempo_confidence");
    openapiFields.add("time_signature");
    openapiFields.add("time_signature_confidence");
    openapiFields.add("window_seconds");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to AudioAnalysisObjectTrack
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!AudioAnalysisObjectTrack.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in AudioAnalysisObjectTrack is not found in the empty JSON string", AudioAnalysisObjectTrack.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!AudioAnalysisObjectTrack.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `AudioAnalysisObjectTrack` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("codestring") != null && !jsonObj.get("codestring").isJsonNull()) && !jsonObj.get("codestring").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `codestring` to be a primitive type in the JSON string but got `%s`", jsonObj.get("codestring").toString()));
      }
      if ((jsonObj.get("echoprintstring") != null && !jsonObj.get("echoprintstring").isJsonNull()) && !jsonObj.get("echoprintstring").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `echoprintstring` to be a primitive type in the JSON string but got `%s`", jsonObj.get("echoprintstring").toString()));
      }
      if ((jsonObj.get("rhythmstring") != null && !jsonObj.get("rhythmstring").isJsonNull()) && !jsonObj.get("rhythmstring").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `rhythmstring` to be a primitive type in the JSON string but got `%s`", jsonObj.get("rhythmstring").toString()));
      }
      if ((jsonObj.get("sample_md5") != null && !jsonObj.get("sample_md5").isJsonNull()) && !jsonObj.get("sample_md5").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `sample_md5` to be a primitive type in the JSON string but got `%s`", jsonObj.get("sample_md5").toString()));
      }
      if ((jsonObj.get("synchstring") != null && !jsonObj.get("synchstring").isJsonNull()) && !jsonObj.get("synchstring").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `synchstring` to be a primitive type in the JSON string but got `%s`", jsonObj.get("synchstring").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!AudioAnalysisObjectTrack.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'AudioAnalysisObjectTrack' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<AudioAnalysisObjectTrack> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(AudioAnalysisObjectTrack.class));

       return (TypeAdapter<T>) new TypeAdapter<AudioAnalysisObjectTrack>() {
           @Override
           public void write(JsonWriter out, AudioAnalysisObjectTrack value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public AudioAnalysisObjectTrack read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of AudioAnalysisObjectTrack given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of AudioAnalysisObjectTrack
   * @throws IOException if the JSON string is invalid with respect to AudioAnalysisObjectTrack
   */
  public static AudioAnalysisObjectTrack fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, AudioAnalysisObjectTrack.class);
  }

  /**
   * Convert an instance of AudioAnalysisObjectTrack to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

