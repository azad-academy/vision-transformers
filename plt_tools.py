from matplotlib import pyplot as plt
import plotly.graph_objects as gplt
from plotly.subplots import make_subplots

def plot_predictions(labels,probs,rows,cols,w,h,save=False):
  

  fig = make_subplots(rows=rows,cols=cols)

  for i in range(0,rows):
    for j in range(0,cols):

      fig.add_trace(gplt.Bar(
          y=labels[j*i+j],
          x=probs[j*i+j],
          name='ImageClassifier',
          orientation='h',
          text = labels[j*i+j],
          textposition="auto",
          insidetextfont=dict(family='Times', size=13, color='white'),
          outsidetextfont=dict(family='Times', size=13, color='black'),
          marker=dict(
              color='rgba(0, 35, 255, 0.6)',
              line=dict(color='rgba(10, 10, 10, 1.0)', width=3)
          )
      ),row=i+1,col=j+1)

  fig.update_layout(autosize=False,width=w,height=h)
  fig.update_yaxes(showticklabels=False)
  fig.update_layout(barmode='stack',showlegend=False,margin=dict(l=0,r=0,b=0,t=1),yaxis=dict(type='category'))
  fig.show(config= dict(displayModeBar = False))

  if(save):
    fig.write_image("predictions.png")