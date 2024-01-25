import { Component, OnInit } from '@angular/core';
import { ArticleService } from '../article.service'
import {CommonModule} from '@angular/common'
import { FormsModule } from '@angular/forms'; // Import FormsModule


@Component({
  selector: 'app-news-article',
  standalone: true,
  imports: [CommonModule,FormsModule],
  templateUrl: './news-article.component.html',
  styleUrl: './news-article.component.css'
})
export class NewsArticleComponent implements OnInit {
  articles: any[] = [];
  loading: boolean = false;
  error: string | null = null;

  constructor(private articleService: ArticleService) { }

  ngOnInit() {
    this.fetchArticles();
  }

  fetchArticles() {
    this.loading = true;
    this.articleService.getAllNews().subscribe(
      (data: any) => {
        this.articles = data;
        this.loading = false;
      },
      (error: any) => {
        this.error = 'Error fetching articles. Please try again later.';
        this.loading = false;
      }
    );
  }
  onSearch() {

  }
  
  onSelect() {

  }
}