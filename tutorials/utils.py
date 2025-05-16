import json
import pandas as pd
from IPython.display import display, HTML

def load_json_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        raise
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in file '{file_path}': {str(e)}")
        raise

from IPython.display import display, HTML
import pandas as pd

from IPython.display import display, HTML
import pandas as pd

from IPython.display import display, HTML
import pandas as pd

from IPython.display import display, HTML
import pandas as pd

from IPython.display import display, HTML
import pandas as pd

def display_scores_as_dataframes(data):
    # Define clean chain labels
    chain_labels = ['Chain 0 (Protein)', 'Chain 1 (ATP)']

    # Create overall scores
    overall_scores = pd.DataFrame({
        'Metric': ['Ranking score', 'pTM', 'ipTM', 'Fraction disordered', 'Has clash'],
        'Value': [
            f"{data['ranking_score']:.2f}",
            f"{data['ptm']:.2f}",
            f"{data['iptm']:.2f}",
            f"{data['fraction_disordered']:.0%}",
            'Yes' if data['has_clash'] else 'No'
        ]
    }).set_index('Metric')

    # Per-chain DataFrame
    per_chain = pd.DataFrame({
        'Chain': chain_labels,
        'iPTM': [f"{x:.2f}" for x in data['chain_iptm']],
        'pTM': [f"{x:.2f}" for x in data['chain_ptm']]
    }).set_index('Chain')

    # Pairwise matrices
    iptm_matrix = pd.DataFrame(
        data['chain_pair_iptm'],
        index=[f'Against {label}' for label in chain_labels],
        columns=chain_labels
    ).map(lambda x: f"{x:.2f}")

    pae_matrix = pd.DataFrame(
        data['chain_pair_pae_min'],
        index=[f'Against {label}' for label in chain_labels],
        columns=chain_labels
    ).map(lambda x: f"{x:.2f}")

    # Convert tables to HTML
    html1 = overall_scores.to_html(classes='df', border=1)
    html2 = per_chain.to_html(classes='df', border=1)
    html3 = iptm_matrix.to_html(classes='df', border=1)
    html4 = pae_matrix.to_html(classes='df', border=1)

    # Display 2x2 grid layout without bold styling
    html_output = f"""
    <style>
        .df {{
            font-family: monospace;
            font-size: 14px;
            width: 100%;
        }}
        table.df td, table.df th {{
            padding: 4px 8px;
            text-align: left;
        }}
        .grid-table {{
            width: 100%;
            table-layout: fixed;
        }}
        .grid-table td {{
            vertical-align: top;
            width: 50%;
            padding: 10px;
        }}
        .section-title {{
            font-size: 15px;
            text-align: center;
            margin-bottom: 6px;
            font-weight: normal;
        }}
    </style>
    <table class="grid-table">
      <tr>
        <td>
          <div class="section-title">Overall Scores</div>
          {html1}
        </td>
        <td>
          <div class="section-title">Per-Chain Metrics</div>
          {html2}
        </td>
      </tr>
      <tr>
        <td>
          <div class="section-title">Pairwise iPTM Matrix</div>
          {html3}
        </td>
        <td>
          <div class="section-title">Pairwise PAE Min Matrix</div>
          {html4}
        </td>
      </tr>
    </table>
    """

    display(HTML(html_output))



# def display_scores_as_dataframes(data):
#     # Create individual DataFrames
#     overall_scores = pd.DataFrame({
#         'Metric': ['Ranking score', 'pTM', 'ipTM', 'Fraction disordered', 'Has clash'],
#         'Value': [
#             f"{data['ranking_score']:.2f}",
#             f"{data['ptm']:.2f}",
#             f"{data['iptm']:.2f}",
#             f"{data['fraction_disordered']:.0%}",
#             'Yes' if data['has_clash'] else 'No'
#         ]
#     }).set_index('Metric')

#     per_chain = pd.DataFrame({
#         'Chain': [f'Chain {i+1}' for i in range(len(data['chain_iptm']))],
#         'iPTM': [f"{x:.2f}" for x in data['chain_iptm']],
#         'pTM': [f"{x:.2f}" for x in data['chain_ptm']]
#     }).set_index('Chain')

#     iptm_matrix = pd.DataFrame(
#         data['chain_pair_iptm'],
#         index=[f'Against Chain {i+1}' for i in range(len(data['chain_pair_iptm']))],
#         columns=[f'Chain {i+1}' for i in range(len(data['chain_pair_iptm'][0]))]
#     ).map(lambda x: f"{x:.2f}")

#     pae_matrix = pd.DataFrame(
#         data['chain_pair_pae_min'],
#         index=[f'Against Chain {i+1}' for i in range(len(data['chain_pair_pae_min']))],
#         columns=[f'Chain {i+1}' for i in range(len(data['chain_pair_pae_min'][0]))]
#     ).map(lambda x: f"{x:.2f}")

#     # Display stacked tables using line breaks
#     display(HTML("<h3> Overall Scores</h3>"))
#     display(overall_scores)
#     display(HTML("<br>"))

#     display(HTML("<h3> Per-Chain Metrics</h3>"))
#     display(per_chain)
#     display(HTML("<br>"))

#     display(HTML("<h3> Pairwise iPTM Matrix</h3>"))
#     display(iptm_matrix)
#     display(HTML("<br>"))

#     display(HTML("<h3> Pairwise PAE Min Matrix</h3>"))
#     display(pae_matrix)


# def display_scores_as_dataframes(data):
#     # Overall Scores DataFrame
#     overall_scores = pd.DataFrame({
#         'Metric': ['Ranking score', 'pTM', 'ipTM', 'Fraction disordered', 'Has clash'],
#         'Value': [
#             f"{data['ranking_score']:.2f}",
#             f"{data['ptm']:.2f}",
#             f"{data['iptm']:.2f}",
#             f"{data['fraction_disordered']:.0%}",
#             'Yes' if data['has_clash'] else 'No'
#         ]
#     }).set_index('Metric')
    
#     # Per-chain metrics DataFrame
#     per_chain = pd.DataFrame({
#         'Chain': [f'Chain {i+1}' for i in range(len(data['chain_iptm']))],
#         'iPTM': [f"{x:.2f}" for x in data['chain_iptm']],
#         'pTM': [f"{x:.2f}" for x in data['chain_ptm']]
#     }).set_index('Chain')
    
#     # Pairwise matrices
#     iptm_matrix = pd.DataFrame(
#         data['chain_pair_iptm'],
#         index=[f'Against Chain {i+1}' for i in range(len(data['chain_pair_iptm']))],
#         columns=[f'Chain {i+1}' for i in range(len(data['chain_pair_iptm'][0]))]
#     ).map(lambda x: f"{x:.2f}")
    
#     pae_matrix = pd.DataFrame(
#         data['chain_pair_pae_min'],
#         index=[f'Against Chain {i+1}' for i in range(len(data['chain_pair_pae_min']))],
#         columns=[f'Chain {i+1}' for i in range(len(data['chain_pair_pae_min'][0]))]
#     ).map(lambda x: f"{x:.2f}")
    
#     # Display all DataFrames with titles
#     print("=== OVERALL SCORES ===")
#     display(overall_scores)
    
#     print("\n=== PER-CHAIN METRICS ===")
#     display(per_chain)
    
#     print("\n=== PAIRWISE iPTM MATRIX ===")
#     display(iptm_matrix)
    
#     print("\n=== PAIRWISE PAE MIN MATRIX ===")
#     display(pae_matrix)
